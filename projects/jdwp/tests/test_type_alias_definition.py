# Copyright (c) Meta Platforms, Inc. and affiliates.

import unittest
from projects.jdwp.defs.schema import PrimitiveType
from projects.jdwp.codegen.new_type_generator import get_type_alias_definition


class TestTypeAliasDefinition(unittest.TestCase):
    def test_specific_type_alias_definitions(self):
        expected_string_type_definition = (
            "StringType = typing.NewType('StringType', str)"
        )
        self.assertEqual(
            get_type_alias_definition(PrimitiveType.STRING),
            expected_string_type_definition,
        )

        expected_boolean_type_definition = (
            "BooleanType = typing.NewType('BooleanType', bool)"
        )
        self.assertEqual(
            get_type_alias_definition(PrimitiveType.BOOLEAN),
            expected_boolean_type_definition,
        )


if __name__ == "__main__":
    unittest.main()
