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
    map_id_type,
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

    def test_map_id_type(self):
        self.assertEqual(map_id_type(IdType.OBJECT_ID), "ObjectIdType")
        self.assertEqual(map_id_type(IdType.THREAD_ID), "ThreadIdType")
        self.assertEqual(map_id_type(IdType.THREAD_GROUP_ID), "ThreadGroupIdType")

    def test_id_type(self):
        self.assertEqual(get_python_type_for_field(IdType.OBJECT_ID), "ObjectIdType")

    def test_integral_type(self):
        self.assertEqual(get_python_type_for_field(IntegralType.INT), "int")

    def test_array_type(self):
        array_type = Array(element_type=IdType.OBJECT_ID, length=1)
        self.assertEqual(get_python_type_for_field(array_type), "List[ObjectIdType]")

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
            simpleField: ObjectIdType
            """
        ).strip()
        self.assertEqual(
            generate_dataclass_for_struct(struct, "SimpleStruct").strip(),
            expected_class_def,
        )

    def test_complex_struct(self):
        struct = Struct(
            fields=[
                Field(name="idField", type=IdType.OBJECT_ID, description=""),
                Field(name="intField", type=IntegralType.INT, description=""),
                Field(
                    name="arrayField",
                    type=Array(element_type=IntegralType.INT, length=1),
                    description="",
                ),
                Field(
                    name="unionField",
                    type=TaggedUnion(tag=None, cases={}),
                    description="",
                ),
            ]
        )
        expected_class_def = dedent(
            """
            @dataclasses.dataclass(frozen=True)
                class ComplexStruct:
            idField: ObjectIdType
            intField: int
            arrayField: List[int]
            unionField: typing.Union[]
            """
        ).strip()
        self.assertEqual(
            generate_dataclass_for_struct(struct, "ComplexStruct").strip(),
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
            idField: ObjectIdType

            
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
