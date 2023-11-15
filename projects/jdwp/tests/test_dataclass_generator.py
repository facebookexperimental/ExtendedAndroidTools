from projects.jdwp.codegen.dataclass_generator import (
    generate_dataclass_for_command,
    generate_dataclass_for_struct,
)
from projects.jdwp.defs.schema import Command, Field, Struct


def test_generate_dataclass_for_struct():
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

    assert generate_dataclass_for_struct(mock_struct, "MockStruct") == expected_output


def test_generate_dataclass_for_command():
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

    assert generate_dataclass_for_command(mock_command) == expected_output
