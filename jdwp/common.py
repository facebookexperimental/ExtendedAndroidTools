"""Basic types for JDWP messages."""

from typing import List


class Types:
    """Types class."""

    STRING = str
    INT = int
    BYTE = float
    BOOLEAN = bool
    DICT = dict
    REFERENCE_TYPE_ID = "referenceTypeID"
    CLASS_LOADER = "classLoader"
    FIELD_ID = "fieldID"
    METHOD_ID = "methodID"
    VALUE = "value"
    INTERFACE_ID = "interfaceID"
    CLASS_OBJECT_ID = "classObjectID"
    TAGGED_OBJECT_ID = "taggedObjectID"
    THREAD_ID = "threadID"
    THREAD_GROUP_ID = "threadGroupID"
    OBJECT_ID = "objectID"
    LOCATION = "location"


class Field:
    """Field class."""

    def __init__(self, name: str, type: str, description: str):
        self.name = name
        self.type = type
        self.description = description


class Struct:
    """Struct class."""

    def __init__(self, fields: List[Field]):
        self.fields = fields


class Command:
    """Command class."""

    def __init__(self, name: str, id: int, out: Struct, reply: Struct):
        self.name = name
        self.id = id
        self.out = out
        self.reply = reply


class CommandSet:
    """Command set class."""

    def __init__(self, name: str, id: int, commands: List[Command]):
        self.name = name
        self.id = id
        self.commands = commands
