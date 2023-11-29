# Copyright (c) Meta Platforms, Inc. and affiliates.

from enum import Enum
from textwrap import dedent
import unittest
from projects.jdwp.defs.schema import (
    IdType,
    IntegralType,
    Array,
    Struct,
    Field,
    Command,
    TaggedUnion,
    UnionTag,
)
from projects.jdwp.codegen.dataclass_generator import (
    format_enum_name,
    get_python_type_for_field,
    generate_dataclass_for_struct,
    generate_dataclass_for_command,
)


class MockEnum(Enum):
    OBJECT_ID = 1
    THREAD_ID = 2
    THREAD_GROUP_ID = 3


class TestJDWPSchema(unittest.TestCase):
    def test_format_enum_name(self):
        self.assertEqual(format_enum_name(MockEnum.OBJECT_ID), "ObjectIdType")
        self.assertEqual(format_enum_name(MockEnum.THREAD_ID), "ThreadIdType")
        self.assertEqual(
            format_enum_name(MockEnum.THREAD_GROUP_ID), "ThreadGroupIdType"
        )

    def test_id_type(self):
        self.assertEqual(get_python_type_for_field(IdType.OBJECT_ID), "ObjectIDType")

    def test_integral_type(self):
        self.assertEqual(get_python_type_for_field(IntegralType.INT), "int")

    def test_array_type(self):
        array_type = Array(element_type=IdType.OBJECT_ID, length=1)
        self.assertEqual(get_python_type_for_field(array_type), "List[ObjectIDType]")

    def test_tagged_union_type(self):
        union_tag = UnionTag(tag=IntegralType.INT, value=IdType.OBJECT_ID)
        tagged_union = TaggedUnion(
            tag=Field(name="tagField", type=union_tag, description=""),
            cases={IdType.OBJECT_ID: Struct([])},
        )

        self.assertEqual(
            get_python_type_for_field(tagged_union, "Parent", "Field"),
            "typing.Union[ParentFieldCaseObjectIdType]",
        )

    def test_struct_type(self):
        struct = Struct(fields=[])
        self.assertEqual(
            get_python_type_for_field(struct, "Parent", "Field"), "ParentField"
        )

    def test_simple_struct(self):
        struct = Struct(
            fields=[Field(name="simpleField", type=IdType.OBJECT_ID, description="")]
        )
        expected_class_def = dedent(
            """
            @dataclasses.dataclass(frozen=True)
            class SimpleStruct:
                simpleField: ObjectIDType
            """
        ).strip()
        self.assertEqual(
            generate_dataclass_for_struct(struct, "SimpleStruct").strip(),
            expected_class_def,
        )

    def test_nested_struct(self):
        nested_struct = Struct(
            fields=[
                Field(
                    name="nestedField",
                    type=Struct(
                        fields=[
                            Field(
                                name="innerField", type=IntegralType.INT, description=""
                            )
                        ]
                    ),
                    description="",
                )
            ]
        )
        expected_class_def = (
            "@dataclasses.dataclass(frozen=True)\n"
            "class NestedStructNestedfield:\n"
            "    innerField: int\n\n"
            "@dataclasses.dataclass(frozen=True)\n"
            "class NestedStruct:\n"
            "    nestedField: NestedStructNestedfield"
        )
        self.assertEqual(
            generate_dataclass_for_struct(nested_struct, "NestedStruct").strip(),
            expected_class_def,
        )

    def test_generate_dataclass_for_command(self):
        out_struct = Struct(
            fields=[Field(name="idField", type=IdType.OBJECT_ID, description="")]
        )
        reply_struct = Struct(
            fields=[Field(name="status", type=IntegralType.INT, description="")]
        )

        command = Command(
            name="SampleCommand", id=1, out=out_struct, reply=reply_struct, error=set()
        )

        expected_output = dedent(
            """
            @dataclasses.dataclass(frozen=True)
            class SampleCommandCommand:
                idField: ObjectIDType
            @dataclasses.dataclass(frozen=True)
            class SampleCommandResponse:
                status: int
            """
        ).strip()

        self.assertEqual(
            generate_dataclass_for_command(command).strip(), expected_output
        )


if __name__ == "__main__":
    unittest.main()
