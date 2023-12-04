# Copyright (c) Meta Platforms, Inc. and affiliates.

import unittest


class JDWPStructTest(unittest.TestCase):
    def test_jdwpstruct_can_be_imported(self):
        from projects.jdwp.runtime.jdwpstruct import JDWPStruct
