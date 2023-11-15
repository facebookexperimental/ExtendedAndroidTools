import unittest
from projects.jdwp.codegen.new_type_generator import get_python_type
from projects.jdwp.defs.schema import PrimitiveType


class TestEnumMemberMapping(unittest.TestCase):
    def test_enum_member_mappings(self):
        for jdwp_type in PrimitiveType:
            with self.subTest(jdwp_type=jdwp_type):
                result = get_python_type(jdwp_type)
                self.assertIsInstance(
                    result, str, f"Mapping for {jdwp_type} is missing or not a string"
                )


if __name__ == "__main__":
    unittest.main()
