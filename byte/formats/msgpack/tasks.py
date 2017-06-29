"""byte-msgpack - tasks module."""
from __future__ import absolute_import, division, print_function

from byte.core.models import StreamTask, StreamReadTask, StreamSelectTask, StreamWriteTask, Task
from byte.formats.msgpack.decoder import MessagePackDecoder
from byte.formats.msgpack.encoder import MessagePackEncoder


class MessagePackTask(StreamTask):
    """MessagePack task base."""

    binary = True

    def __init__(self, executor):
        """Create MessagePack task.

        :param executor: Executor
        :type executor: byte.executors.file.FileTableExecutor
        """
        super(MessagePackTask, self).__init__(executor)

        self.format = None


class MessagePackReadTask(StreamReadTask, MessagePackTask):
    """MessagePack read task."""

    def __init__(self, fmt, executor, operation):
        """Create MessagePack read task.

        :param executor: Executor
        :type executor: byte.executors.core.base.Executor

        :param operation: Read operation
        :type operation: byte.compilers.core.models.Operation
        """
        super(MessagePackReadTask, self).__init__(executor, operation)

        self.format = fmt

        self.decoder = None

    def open(self):
        """Open task."""
        super(MessagePackReadTask, self).open()

        # Create decoder
        self.decoder = MessagePackDecoder(self.format, self.stream)


class MessagePackSelectTask(StreamSelectTask, MessagePackReadTask):
    """MessagePack select task."""

    def decode(self):
        """Decode items."""
        return self.decoder.items()


class MessagePackWriteTask(StreamWriteTask, MessagePackTask):
    """MessagePack write task."""

    def __init__(self, fmt, executor, operations):
        """Create MessagePack write task.

        :param executor: Executor
        :type executor: byte.executors.core.base.Executor

        :param operations: Write operations
        :type operations: list of byte.compilers.core.models.Operation
        """
        super(MessagePackWriteTask, self).__init__(executor, operations)

        self.format = fmt

        self.decoder = None

    @property
    def state(self):
        """Retrieve task state.

        :rtype: int
        """
        state = super(MessagePackWriteTask, self).state

        if self.decoder is None or state == Task.State.created:
            return Task.State.created

        if self.decoder.closed or state == Task.State.closed:
            return Task.State.closed

        return Task.State.started

    def decode(self):
        """Decode items."""
        return self.decoder.items()

    def encode(self, revision, items):
        """Encode items.

        :param revision: Executor revision
        :type revision: byte.executors.file.revision.FileRevision

        :param items: Items to encode
        :type items: dict or list
        """
        # Create encoder
        encoder = MessagePackEncoder(
            self.format,
            revision.stream
        )

        # Encode items, and write to revision stream
        encoder.encode(items)

    def open(self):
        """Open task."""
        super(MessagePackWriteTask, self).open()

        # Create decoder
        self.decoder = MessagePackDecoder(self.format, self.stream)

    def close(self):
        """Close task."""
        if not super(MessagePackWriteTask, self).close():
            return False

        # Close decoder
        if self.decoder:
            self.decoder.close()

        return True
