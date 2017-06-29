"""byte-msgpack - decoder module."""
from __future__ import absolute_import, division, print_function

from byte.formats.msgpack.models import MessagePackCollectionStructure

from msgpack import Unpacker
import six


class MessagePackDecoder(object):
    """MessagePack decoder class."""

    def __init__(self, fmt, stream):
        """Create MessagePack decoder.
        
        :param stream: Stream
        :type stream: file or io.IOBase
        """
        self.format = fmt
        self.stream = stream

    @property
    def closed(self):
        """Retrieve boolean representing the decoder "closed" status."""
        return self.stream is None

    def items(self):
        """Decode items from stream."""
        if self.format.structure == MessagePackCollectionStructure.Dictionary:
            return self._decode_dictionary()

        if self.format.structure == MessagePackCollectionStructure.List:
            return self._decode_list()

        if self.format.structure == MessagePackCollectionStructure.Objects:
            return self._decode_objects()

        raise ValueError('Invalid decoder mode: %s' % (self.format.structure,))

    def close(self):
        """Close decoder."""
        if self.stream is None:
            return

        self.stream = None

    def _decode_dictionary(self):
        unpacker = Unpacker(self.stream)

        for items in unpacker:
            if not items:
                continue

            if type(items) is not dict:
                raise ValueError('Invalid item, expected dictionary, found: %s' % (type(items).__name__,))

            for item in six.itervalues(items):
                yield item

    def _decode_list(self):
        unpacker = Unpacker(self.stream)

        for items in unpacker:
            if not items:
                continue

            if type(items) is not list:
                raise ValueError('Invalid item, expected list, found: %s' % (type(items).__name__,))

            for item in items:
                yield item

    def _decode_objects(self):
        unpacker = Unpacker(self.stream)

        for item in unpacker:
            if not item:
                continue

            if type(item) is not dict:
                raise ValueError('Invalid item, expected dictionary, found: %s' % (type(item).__name__,))

            yield item
