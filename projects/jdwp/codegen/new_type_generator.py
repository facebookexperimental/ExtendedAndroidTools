"""New type Generator."""
from projects.jdwp.defs.schema import PrimitiveType


def get_python_type(jdwp_type: PrimitiveType) -> str:
    """Map JDWP type to Python type."""
    mapping = {
        PrimitiveType.STRING: "str",
        PrimitiveType.INT: "int",
        PrimitiveType.BYTE: "int",
        PrimitiveType.BOOLEAN: "bool",
    }
    return mapping.get(jdwp_type, "int")


def generate_new_types():
    for type_name, jdwp_type in PrimitiveType.__members__.items():
        python_type = get_python_type(jdwp_type.value)
        newtype_name = f"{type_name.capitalize()}Type"
        print(f"{newtype_name} = NewType('{newtype_name}', {python_type})")
