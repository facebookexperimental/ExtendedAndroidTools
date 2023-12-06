# Copyright (c) Meta Platforms, Inc. and affiliates.

import unittest


class ImportTest(unittest.TestCase):
    def test_structs_can_be_imported(self):
        from projects.jdwp.runtime.structs import IDSizesReply

    def test_type_aliases_can_be_imported(self):
        from projects.jdwp.runtime.type_aliases import ReferenceTypeIDType

    def test_jdwpstruct_can_be_imported(self):
        from projects.jdwp.runtime.jdwpstruct import JDWPStruct

    def test_streams_can_be_imported(self):
        from projects.jdwp.runtime.async_streams import JDWPInputStreamBase
