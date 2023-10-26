# Copyright (c) Meta Platforms, Inc. and affiliates.

"""JDWP Commands for ThreadReference Command Set."""

from projects.jdwp.defs.schema import Command, Field, Struct, Type
from projects.jdwp.constants.errors import ErrorConstants

Name = Command(
    name="Name",
    id=1,
    out=Struct([Field("threadID", Type.THREAD_ID, "The thread object ID.")]),
    reply=Struct([Field("threadName", Type.STRING, "The thread name.")]),
    error=Struct(
        [
            Field(
                "INVALID_THREAD",
                ErrorConstants.INVALID_THREAD,
                "Passed thread is null, is not a valid thread or has exited.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "thread is not a known ID.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)


Suspend = Command(
    name="Suspend",
    id=2,
    out=Struct([Field("threadID", Type.THREAD_ID, "The thread object ID.")]),
    reply=Struct([]),
    error=Struct(
        [
            Field(
                "INVALID_THREAD",
                ErrorConstants.INVALID_THREAD,
                "Passed thread is null, is not a valid thread or has exited.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "thread is not a known ID.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)

Resume = Command(
    name="Resume",
    id=3,
    out=Struct([Field("threadID", Type.THREAD_ID, "The thread object ID.")]),
    reply=Struct([]),
    error=Struct(
        [
            Field(
                "INVALID_THREAD",
                ErrorConstants.INVALID_THREAD,
                "Passed thread is null, is not a valid thread or has exited.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "thread is not a known ID.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)

Status = Command(
    name="Status",
    id=4,
    out=Struct([Field("threadID", Type.THREAD_ID, "The thread object ID.")]),
    reply=Struct(
        [
            Field(
                "threadStatus",
                Type.INT,
                "One of the thread status codes. See JDWP.ThreadStatus",
            ),
            Field(
                "suspendStatus",
                Type.INT,
                "One of the suspend status codes. See JDWP.SuspendStatus",
            ),
        ]
    ),
    error=Struct(
        [
            Field(
                "INVALID_THREAD",
                ErrorConstants.INVALID_THREAD,
                "Passed thread is null, is not a valid thread or has exited.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "thread is not a known ID.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)

ThreadGroup = Command(
    name="Thread group",
    id=5,
    out=Struct([Field("threadID", Type.THREAD_ID, "The thread object ID.")]),
    reply=Struct(
        [
            Field(
                "threadGroupID",
                Type.THREAD_GROUP_ID,
                "The thread group of this thread.",
            )
        ]
    ),
    error=Struct(
        [
            Field(
                "INVALID_THREAD",
                ErrorConstants.INVALID_THREAD,
                "Passed thread is null, is not a valid thread or has exited.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "thread is not a known ID.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)

Frames = Command(
    name="Frames",
    id=6,
    out=Struct(
        [
            Field("threadID", Type.THREAD_ID, "The thread object ID."),
            Field("startFrame", Type.INT,
                  "The index of the first frame to retrieve."),
            Field(
                "length",
                Type.INT,
                "The count of frames to retrieve (-1 means all remaining).",
            ),
        ]
    ),
    reply=Struct(
        [
            Field("frames", Type.INT, "The number of frames retrieved"),
            Field("frameID", Type.FRAME_ID, "The ID of this frame."),
            Field("location", Type.LOCATION, "The location of this frame."),
        ]
    ),
    error=Struct(
        [
            Field(
                "INVALID_THREAD",
                ErrorConstants.INVALID_THREAD,
                "Passed thread is null, is not a valid thread or has exited.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "thread is not a known ID.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)

FrameCount = Command(
    name="Frame count",
    id=7,
    out=Struct([Field("threadID", Type.THREAD_ID, "The thread object ID.")]),
    reply=Struct(
        [Field("frameCount", Type.INT, "The count of frames on this thread's stack.")]
    ),
    error=Struct(
        [
            Field(
                "INVALID_THREAD",
                ErrorConstants.INVALID_THREAD,
                "Passed thread is null, is not a valid thread or has exited.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "thread is not a known ID.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)

OwnedMonitors = Command(
    name="Owned monitors",
    id=8,
    out=Struct([Field("threadID", Type.THREAD_ID, "The thread object ID.")]),
    reply=Struct(
        [
            Field("owned", Type.INT, "The number of owned monitors"),
            Field("monitor", Type.TAGGED_OBJECT_ID, "An owned monitor"),
        ]
    ),
    error=Struct(
        [
            Field(
                "INVALID_THREAD",
                ErrorConstants.INVALID_THREAD,
                "Passed thread is null, is not a valid thread or has exited.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "thread is not a known ID.",
            ),
            Field(
                "NOT IMPLEMENTED",
                ErrorConstants.NOT_IMPLEMENTED,
                "The functionality is not implemented in this virtual machine.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)

CurrentContendedMonitor = Command(
    name="Current contended monitor",
    id=9,
    out=Struct([Field("threadID", Type.THREAD_ID, "The thread object ID.")]),
    reply=Struct(
        [
            Field(
                "monitor",
                Type.OBJECT_ID,
                "The contended monitor, or null if there is no current contended monitor.",
            )
        ]
    ),
    error=Struct(
        [
            Field(
                "INVALID_THREAD",
                ErrorConstants.INVALID_THREAD,
                "Passed thread is null, is not a valid thread or has exited.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "thread is not a known ID.",
            ),
            Field(
                "NOT IMPLEMENTED",
                ErrorConstants.NOT_IMPLEMENTED,
                "The functionality is not implemented in this virtual machine.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)

Stop = Command(
    name="Stop",
    id=10,
    out=Struct(
        [
            Field("threadID", Type.THREAD_ID, "The thread object ID."),
            Field(
                "throwable",
                Type.OBJECT_ID,
                "Asynchronous exception. This object must be an instance of java.lang.Throwable or a subclass",
            ),
        ]
    ),
    reply=Struct([]),
    error=Struct(
        [
            Field(
                "INVALID_THREAD",
                ErrorConstants.INVALID_THREAD,
                "Passed thread is null, is not a valid thread or has exited.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "thread is not a known ID.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)

Interrupt = Command(
    name="Interrupt",
    id=11,
    out=Struct([Field("threadID", Type.THREAD_ID, "The thread object ID.")]),
    reply=Struct([]),
    error=Struct(
        [
            Field(
                "INVALID_THREAD",
                ErrorConstants.INVALID_THREAD,
                "Passed thread is null, is not a valid thread or has exited.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "thread is not a known ID.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)

SuspendCount = Command(
    name="Suspend count",
    id=12,
    out=Struct([Field("threadID", Type.THREAD_ID, "The thread object ID.")]),
    reply=Struct(
        [
            Field(
                "suspendCount",
                Type.INT,
                "The number of outstanding suspends of this thread.",
            )
        ]
    ),
    error=Struct(
        [
            Field(
                "INVALID_THREAD",
                ErrorConstants.INVALID_THREAD,
                "Passed thread is null, is not a valid thread or has exited.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "thread is not a known ID.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)

OwnedMonitorsStackDepthInfo = Command(
    name="Owned monitors stack depth info",
    id=13,
    out=Struct([Field("threadID", Type.THREAD_ID, "The thread object ID.")]),
    reply=Struct(
        [
            Field("owned", Type.INT, "The number of owned monitors"),
            Field("monitor", Type.TAGGED_OBJECT_ID, "An owned monitor"),
            Field(
                "stack_depth",
                Type.INT,
                "Stack depth location where monitor was acquired",
            ),
        ]
    ),
    error=Struct(
        [
            Field(
                "INVALID_THREAD",
                ErrorConstants.INVALID_THREAD,
                "Passed thread is null, is not a valid thread or has exited.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "thread is not a known ID.",
            ),
            Field(
                "NOT IMPLEMENTED",
                ErrorConstants.NOT_IMPLEMENTED,
                "The functionality is not implemented in this virtual machine.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)

ForceEarlyReturn = Command(
    name="Force early return",
    id=14,
    out=Struct(
        [
            Field("threadID", Type.THREAD_ID, "The thread object ID."),
            Field("value", Type.VALUE, "The value to return."),
        ]
    ),
    reply=Struct([]),
    error=Struct(
        [
            Field(
                "INVALID_THREAD",
                ErrorConstants.INVALID_THREAD,
                "Passed thread is null, is not a valid thread or has exited.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "thread is not a known ID.",
            ),
            Field(
                "THREAD_NOT_SUSPENDED",
                ErrorConstants.THREAD_NOT_SUSPENDED,
                "If the specified thread has not been suspended by an event.",
            ),
            Field(
                "THREAD_NOT_ALIVE",
                ErrorConstants.THREAD_NOT_ALIVE,
                "Thread has not been started or is now dead.",
            ),
            Field(
                "OPAQUE_FRAME",
                ErrorConstants.OPAQUE_FRAME,
                "Attempted to return early from a frame corresponding to a native method. Or the implementation is unable to provide this functionality on this frame.",
            ),
            Field(
                "NO_MORE_FRAMES",
                ErrorConstants.NO_MORE_FRAMES,
                "There are no more Java or JNI frames on the call stack.",
            ),
            Field(
                "NOT IMPLEMENTED",
                ErrorConstants.NOT_IMPLEMENTED,
                "The functionality is not implemented in this virtual machine.",
            ),
            Field(
                "TYPE_MISMATCH",
                ErrorConstants.TYPE_MISMATCH,
                "Value is not an appropriate type for the return value of the method.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)
