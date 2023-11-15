from textwrap import dedent

from projects.jdwp.defs.schema import Command, Struct


def generate_dataclass_for_command(command: Command) -> str:
    """Generates a dataclass definition for a given command."""
    out_class = (
        generate_dataclass_for_struct(command.out, f"{command.name}Command")
        if command.out
        else ""
    )

    reply_class = (
        generate_dataclass_for_struct(command.reply, f"{command.name}Response")
        if command.reply
        else ""
    )

    return out_class + "\n" + reply_class


def generate_dataclass_for_struct(struct: Struct, class_name: str) -> str:
    """Generates a dataclass definition for a given struct."""
    fields_def = "\n".join(f"    {field.name}: {field.type}" for field in struct.fields)
    class_def = dedent(
        f"""
    @dataclasses.dataclass(frozen=True)
    class {class_name}:
{fields_def}
    """
    )
    return class_def
