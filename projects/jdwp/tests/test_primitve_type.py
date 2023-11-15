import pytest
from projects.jdwp.codegen.new_type_generator import get_python_type
from projects.jdwp.defs.schema import PrimitiveType


@pytest.mark.parametrize("jdwp_type", PrimitiveType)
def test_enum_member_mapping(jdwp_type):
    result = get_python_type(jdwp_type)
    assert isinstance(
        result, str
    ), f"Mapping for {jdwp_type} is missing or not a string"
