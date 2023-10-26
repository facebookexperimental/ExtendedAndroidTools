# Copyright (c) Meta Platforms, Inc. and affiliates.

"""Command Set: ThreadReference."""

from projects.jdwp.defs.schema import CommandSet
from projects.jdwp.defs.commands.thread_reference import (
    Name,
    Suspend,
    Resume,
    Status,
    ThreadGroup,
    Frames,
    FrameCount,
    OwnedMonitors,
    CurrentContendedMonitor,
    Stop,
    Interrupt,
    SuspendCount,
    OwnedMonitorsStackDepthInfo,
    ForceEarlyReturn,
)

ThreadReference = CommandSet(
    name="ThreadReference",
    id=11,
    commands=[
        Name,
        Suspend,
        Resume,
        Status,
        ThreadGroup,
        Frames,
        FrameCount,
        OwnedMonitors,
        CurrentContendedMonitor,
        Stop,
        Interrupt,
        SuspendCount,
        OwnedMonitorsStackDepthInfo,
        ForceEarlyReturn,
    ],
)
