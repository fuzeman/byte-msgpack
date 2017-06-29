"""byte-msgpack - format module."""
from __future__ import absolute_import, division, print_function

from byte.formats.core.base import CollectionFormatPlugin, DocumentFormatPlugin, Format
from byte.formats.msgpack.models import MessagePackCollectionStructure
from byte.formats.msgpack.tasks import MessagePackSelectTask, MessagePackWriteTask


class BaseMessagePackFormat(Format):
    """MessagePack base format."""

    pass


class MessagePackCollectionFormat(BaseMessagePackFormat, CollectionFormatPlugin):
    """MessagePack collection format."""

    Structure = MessagePackCollectionStructure

    key = 'msgpack:collection'

    class Meta(CollectionFormatPlugin.Meta):
        """MessagePack collection format metadata."""

        content_type = [
            'application/msgpack',
            'application/x-msgpack'
        ]

        extension = [
            'msgpack',
            'mpack'
        ]

    def __init__(self, structure=MessagePackCollectionStructure.Objects):
        self.structure = structure

    def insert(self, executor, operation):
        """Execute insert operation.

        :param executor: Executor
        :type executor: byte.executors.core.base.Executor

        :param operation: Insert operation
        :type operation: byte.compilers.core.models.InsertOperation
        """
        return MessagePackWriteTask(self, executor, [operation]).execute()

    def select(self, executor, operation):
        """Execute select operation.

        :param executor: Executor
        :type executor: byte.executors.core.base.Executor

        :param operation: Select operation
        :type operation: byte.compilers.core.models.SelectOperation
        """
        return MessagePackSelectTask(self, executor, operation).execute()


class MessagePackDocumentFormat(DocumentFormatPlugin):
    """MessagePack document format."""

    key = 'msgpack:document'

    class Meta(DocumentFormatPlugin.Meta):
        """MessagePack document format metadata."""

        content_type = [
            'application/msgpack',
            'application/x-msgpack'
        ]

        extension = [
            'msgpack',
            'mpack'
        ]
