"""New type Generator."""
from projects.jdwp.defs.schema import PrimitiveType
import typing


def get_python_type(jdwp_type: PrimitiveType) -> str:
    """Map JDWP type to Python type."""
    mapping = {
        PrimitiveType.STRING: "str",
        PrimitiveType.INT: "int",
        PrimitiveType.BYTE: "int",
        PrimitiveType.BOOLEAN: "bool",
    }
    return mapping.get(jdwp_type, "int")


def get_type_alias_definition(jdwp_type: PrimitiveType) -> str:
    """Return the type alias definition for a given JDWP type."""
    python_type = get_python_type(jdwp_type)
    new_type_name = f"{jdwp_type.name.capitalize()}Type"
    return f"{new_type_name} = typing.NewType('{new_type_name}', {python_type})"


def generate_new_types():
    for jdwp_type in PrimitiveType:
        type_alias_definition = get_type_alias_definition(jdwp_type)
        print(type_alias_definition)
