import pytest
from projects.jdwp.defs.schema import PrimitiveType
from projects.jdwp.codegen.new_type_generator import get_type_alias_definition


@pytest.mark.parametrize("jdwp_type", PrimitiveType)
def test_type_alias_definition(jdwp_type):
    expected_start = f"{jdwp_type.name.capitalize()}Type = NewType"
    definition = get_type_alias_definition(jdwp_type)
    assert definition.startswith(
        expected_start
    ), f"Definition for {jdwp_type} is incorrect"
