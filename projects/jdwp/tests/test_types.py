# Copyright (c) Meta Platforms, Inc. and affiliates.

import unittest
from projects.jdwp.codegen.types import python_type_for
from projects.jdwp.defs.schema import IdType


class TestTypesMapping(unittest.TestCase):
    def test_id_type_mapping(self):
        for id_type in IdType:
            with self.subTest(id_type=id_type):
                result = python_type_for(id_type)
                self.assertIsInstance(
                    result, str, f"Mapping for {id_type} is missing or not a string"
                )
