# Copyright (c) Meta Platforms, Inc. and affiliates.

import unittest
from projects.jdwp.defs.schema import IdType
from projects.jdwp.codegen.new_type_generator import get_type_alias_definition


class TestTypeAliasDefinition(unittest.TestCase):
    def test_specific_type_alias_definitions(self):
        expected_object_id_type_definition = (
            "ObjectIDType = typing.NewType('ObjectIDType', int)"
        )
        self.assertEqual(
            get_type_alias_definition(IdType.OBJECT_ID),
            expected_object_id_type_definition,
        )
