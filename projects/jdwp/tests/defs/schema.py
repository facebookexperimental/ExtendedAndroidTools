# Copyright (c) Meta Platforms, Inc. and affiliates.

import unittest


class SchemaTests(unittest.TestCase):
    def test_schema_can_be_imported(self):
        from projects.jdwp.defs.schema import PrimitiveType
