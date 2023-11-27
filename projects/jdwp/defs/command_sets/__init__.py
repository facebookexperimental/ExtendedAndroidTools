# Copyright (c) Meta Platforms, Inc. and affiliates.

from projects.jdwp.defs.command_sets.virtual_machine import VirtualMachine
from projects.jdwp.defs.command_sets.reference_type import ReferenceType
from projects.jdwp.defs.command_sets.event_request import EventRequest

ALL = [
    VirtualMachine,
    ReferenceType,
    EventRequest,
]
