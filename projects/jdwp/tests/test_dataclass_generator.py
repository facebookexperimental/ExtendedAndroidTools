import unittest
from projects.jdwp.codegen.dataclass_generator import (
    generate_dataclass_for_command,
    generate_dataclass_for_struct,
)
from projects.jdwp.defs.schema import Command, Field, Struct


class TestDataclassGenerator(unittest.TestCase):
    def test_generate_dataclass_for_struct(self):
        # Create a mock Struct
        mock_struct = Struct(
            fields=[
                Field(name="field1", type="int", description="An integer field"),
                Field(name="field2", type="str", description="A string field"),
            ]
        )

        expected_output = (
            "@dataclasses.dataclass(frozen=True)\n"
            "class MockStruct:\n"
            "    field1: int\n"
            "    field2: str\n"
        )

        self.assertEqual(
            generate_dataclass_for_struct(mock_struct, "MockStruct"), expected_output
        )

    def test_generate_dataclass_for_command(self):
        mock_command = Command(
            name="TestCommand",
            id=1,
            out=Struct(fields=[Field(name="outField", type="int", description="")]),
            reply=Struct(fields=[Field(name="replyField", type="str", description="")]),
            error=set(),
        )

        expected_output = (
            "@dataclasses.dataclass(frozen=True)\n"
            "class TestCommandCommand:\n"
            "    outField: int\n\n"
            "@dataclasses.dataclass(frozen=True)\n"
            "class TestCommandResponse:\n"
            "    replyField: str\n"
        )

        self.assertEqual(generate_dataclass_for_command(mock_command), expected_output)


if __name__ == "__main__":
    unittest.main()
