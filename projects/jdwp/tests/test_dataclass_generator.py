# Copyright (c) Meta Platforms, Inc. and affiliates.

import unittest
from projects.jdwp.defs.schema import ArrayLength, IntegralType, Struct, Field, Array
from projects.jdwp.codegen.dataclass_generator import StructGenerator


class TestStructGenerator(unittest.TestCase):
    def test_simple_struct(self):
        simple_struct = Struct(
            fields=[
                Field(name="id", type=IntegralType.INT, description="An integer ID")
            ]
        )

        generator = StructGenerator(simple_struct, "SimpleStruct")

        result = generator.generate()

        expected = [
            "@dataclasses.dataclass(frozen=True)\n"
            "class SimpleStruct:\n"
            "    id: int"
        ]

        self.assertEqual(result, expected)

    def test_nested_struct(self):
        inner_struct = Struct(
            fields=[
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

        self.assertEqual(result, expected)

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

        array_length = ArrayLength(type=IntegralType.INT)

        array_struct = Struct(
            fields=[
                Field(
                    name="array",
                    type=Array(
                        element_type=element_struct,
                        length=Field(
                            name="length", type=array_length, description="Array length"
                        ),
                    ),
                    description="Array of structures",
                )
            ]
        )

        generator = StructGenerator(array_struct, "ArrayStruct")

        result = generator.generate()

        expected = [
            "@dataclasses.dataclass(frozen=True)\n"
            "class ArrayStructArrayElement:\n"
            "    element_field: int",
            "@dataclasses.dataclass(frozen=True)\n"
            "class ArrayStruct:\n"
            "    array: typing.List[ArrayStructArrayElement]",
        ]

        self.assertEqual(result, expected)
