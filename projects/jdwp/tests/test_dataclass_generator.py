import unittest
from projects.jdwp.defs.schema import Struct, Field, Array, TaggedUnion
from projects.jdwp.codegen.dataclass_generator import StructGenerator


class TestStructGenerator(unittest.TestCase):
    def test_simple_struct(self):
        simple_struct = Struct(fields=[Field(name="id", type="int", description="")])
        generator = StructGenerator(simple_struct, "SimpleStruct")
        expected = [
            "@dataclasses.dataclass(frozen=True)\n"
            "class SimpleStruct:\n"
            "    id: int"
        ]
        self.assertEqual(generator.generate(), expected)

    def test_nested_struct(self):
        nested_struct = Struct(
            fields=[
                Field(
                    name="nested",
                    type=Struct(
                        fields=[Field(name="inner", type="int", description="")]
                    ),
                    description="",
                )
            ]
        )
        generator = StructGenerator(nested_struct, "NestedStruct")
        expected = [
            "@dataclasses.dataclass(frozen=True)\n"
            "class NestedStructNested:\n"
            "    inner: int",
            "@dataclasses.dataclass(frozen=True)\n"
            "class NestedStruct:\n"
            "    nested: NestedStructNested",
        ]
        self.assertEqual(generator.generate(), expected)

    def test_struct_in_array(self):
        array_struct = Struct(
            fields=[
                Field(
                    name="arrayField",
                    type=Array(
                        element_type=Struct(
                            fields=[
                                Field(name="elementField", type="int", description="")
                            ]
                        ),
                        length=1,
                    ),
                    description="",
                )
            ]
        )
        generator = StructGenerator(array_struct, "ArrayStruct")
        expected = [
            "@dataclasses.dataclass(frozen=True)\n"
            "class ArrayStructArrayFieldElement:\n"
            "    elementField: int",
            "@dataclasses.dataclass(frozen=True)\n"
            "class ArrayStruct:\n"
            "    arrayField: typing.List[ArrayStructArrayFieldElement]",
        ]
        self.assertEqual(generator.generate(), expected)


if __name__ == "__main__":
    unittest.main()
