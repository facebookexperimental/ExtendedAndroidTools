# Copyright (c) Meta Platforms, Inc. and affiliates.

from textwrap import dedent
import unittest
from projects.jdwp.defs.schema import (
    ArrayLength,
    IntegralType,
    OpaqueType,
    Struct,
    Field,
    Array,
)
from projects.jdwp.codegen.dataclass_generator import (
    StructGenerator,
    compute_struct_names,
)


class TestStructGenerator(unittest.TestCase):
    maxDiff = None

        generator = StructGenerator(simple_struct, "SimpleStruct")

        result = generator.generate()

        expected = [
            "@dataclasses.dataclass(frozen=True)\n"
            "class SimpleStruct:\n"
            "    id: int"
        ]

        self.assertSequenceEqual(list(result), expected)

    def test_nested_struct(self):
        inner_struct = Struct(
            fields=[
                Field(name="id", type=IntegralType.INT, description="An integer ID"),
                Field(name="name", type=OpaqueType.STRING, description="Name"),
                Field(
                    name="inner_field",
                    type=IntegralType.INT,
                    description="Inner integer field",
                )
            ]
        )
        outer_struct = Struct(
            fields=[
                Field(name="nested", type=inner_struct, description="Nested structure")
            ]
        )

        generator = StructGenerator(outer_struct, "OuterStruct")

        result = generator.generate()

        expected = [
            "@dataclasses.dataclass(frozen=True)\n"
            "class OuterStructNested:\n"
            "    inner_field: int",
            "@dataclasses.dataclass(frozen=True)\n"
            "class OuterStruct:\n"
            "    nested: OuterStructNested",
        ]

        self.assertSequenceEqual(list(result), expected)

    def test_struct_in_array(self):
        # Define a structure
        element_struct = Struct(
            fields=[
                Field(
                    name="element_field",
                    type=IntegralType.INT,
                    description="Element field",
                )
            ]
        )

        array_length = Field(
            name="length",
            type=ArrayLength(type=IntegralType.INT),
            description="Array length",
        )

        array_struct = Struct(
            fields=[
                array_length,
                Field(
                    name="array of elements",
                    type=Array(
                        element_type=element_struct,
                        length=array_length,
                    ),
                    description="Array of structures",
                ),
            ]
        )
        struct_names = compute_struct_names(test_struct, "TestStruct")

        generator = StructGenerator(test_struct, struct_names)

        result_str = "\n".join(generator.generate())

        expected = dedent(
            """
        @dataclasses.dataclass(frozen=True)
        class TestStruct:
            id: int
            name: str
            values: typing.List[int]

        def serialize(self, output: JDWPOutputStreamBase):
            output.write_int(self.id)
            output.write_string(self.name)
            output.write_int(len(self.values))  # Write dynamic array length
        for element in self.values:
            if element is not None:
                element.serialize(output)  # Serialize each element



        result = generator.generate()

        expected = [
            "@dataclasses.dataclass(frozen=True)\n"
            "class ArrayStructArrayOfElementsElement:\n"
            "    element_field: int",
            "@dataclasses.dataclass(frozen=True)\n"
            "class ArrayStruct:\n"
            "    arrayOfElements: typing.List[ArrayStructArrayOfElementsElement]",
        ]

        self.assertSequenceEqual(list(result), expected)
