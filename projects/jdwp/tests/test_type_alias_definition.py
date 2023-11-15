import unittest
from projects.jdwp.defs.schema import PrimitiveType
from projects.jdwp.codegen.new_type_generator import get_type_alias_definition


class TestTypeAliasDefinition(unittest.TestCase):
    def test_type_alias_definitions(self):
        for jdwp_type in PrimitiveType:
            with self.subTest(jdwp_type=jdwp_type):
                expected_start = f"{jdwp_type.name.capitalize()}Type = NewType"
                definition = get_type_alias_definition(jdwp_type)
                self.assertTrue(
                    definition.startswith(expected_start),
                    f"Definition for {jdwp_type} is incorrect",
                )


if __name__ == "__main__":
    unittest.main()
