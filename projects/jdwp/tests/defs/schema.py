# Copyright (c) Meta Platforms, Inc. and affiliates.

import unittest


class SchemaTests(unittest.TestCase):
    def test_schema_can_be_imported(self):
        from projects.jdwp.defs.schema import OpaqueType

    def test_command_sets_are_hashable(self):
        from projects.jdwp.defs.command_sets import (
            event_request,
            reference_type,
            virtual_machine,
        )

        hash(event_request.EventRequest)
        hash(reference_type.ReferenceType)
        hash(event_request.EventRequest)
