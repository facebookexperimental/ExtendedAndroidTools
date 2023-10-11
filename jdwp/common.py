"""Basic types for JDWP messages."""


class Type:
    pass


class String(Type):
    pass


class Int(Type):
    pass


# Define Field class
class Field:
    def __init__(self, name, type):
        self.name = name
        self.type = type


# Define Struct class
class Struct:
    def __init__(self, fields):
        self.fields = fields


# Define Command class
class Command:
    def __init__(self, name, id, out, reply):
        self.name = name
        self.id = id
        self.out = out
        self.reply = reply


# Define CommandSet class
class CommandSet:
    def __init__(self, name, id, commands):
        self.name = name
        self.id = id
        self.commands = commands


# Create JDWP message descriptions
Version = Command(
    name="version",
    id=1,
    out=None,
    reply=Struct(
        [
            Field("description", String),
            Field("jdwp major", Int),
            Field("jdwp minor", Int),
            Field("vm version", String),
            Field("vm name", String),
        ]
    ),
)

ClassesBySignature = Command(
    name="classes by signature",
    id=2,
    out=Struct(
        [
            Field("signature", String),
        ]
    ),
    reply=Struct(
        [
            # ... (other fields)
        ]
    ),
)

VirtualMachine = CommandSet(
    name="VirtualMachine",
    id=1,
    commands=[
        Version,
        ClassesBySignature,
    ],
)
