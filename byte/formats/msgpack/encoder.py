"""byte-msgpack - encoder module."""
from __future__ import absolute_import, division, print_function

from byte.formats.msgpack.models import MessagePackCollectionStructure

from msgpack import Packer
import six


class MessagePackEncoder(object):
    """MessagePack Encoder."""

    def __init__(self, fmt, stream, **kwargs):
        """Create MessagePack Encoder.

        :param stream: Output stream
        :type stream: file or io.IOBase
        """
        self.format = fmt
        self.stream = stream

        self.packer = Packer(**kwargs)

    def encode(self, items):
        """Encode items.

        :param items: Items
        :type items: generator
        """
        if self.format.structure == MessagePackCollectionStructure.Dictionary:
            return self._encode_dictionary(items)

        if self.format.structure == MessagePackCollectionStructure.List:
            return self._encode_list(items)

        if self.format.structure == MessagePackCollectionStructure.Objects:
            return self._encode_objects(items)

        raise ValueError('Invalid encoder mode: %s' % (self.format.structure,))

    def _encode_dictionary(self, items):
        """Encode :code:`items` to dictionary.

        :param items: Items
        :type items: generator
        """
        self.stream.write(self.packer.pack(DictionaryEmitter(items)))

    def _encode_list(self, items):
        """Encode :code:`items` to list.

        :param items: Items
        :type items: generator
        """
        raise NotImplementedError

    def _encode_objects(self, items):
        """Encode :code:`items` to individual objects.

        :param items: Items
        :type items: generator
        """
        for _, item in items:
            self.stream.write(self.packer.pack(item))


class DictionaryEmitter(dict):
    """MessagePack dictionary emitter."""

    def __init__(self, items):
        """Create MessagePack dictionary emitter.

        :param items: Items
        :type items: generator
        """
        super(DictionaryEmitter, self).__init__()

        self._items = items

    def items(self):
        """Retrieve item iterator."""
        if six.PY2:
            raise Exception('DictionaryEmitter.items() is not supported')

        return self.iteritems()

    def iteritems(self):
        """Retrieve item iterator."""
        for item in self._items:
            yield item

    def __bool__(self):
        """Return boolean representation of instance."""
        return True

    def __nonzero__(self):
        """Return boolean indicating the instance is non-zero."""
        return True

    def __repr__(self):
        """Return python representation of instance."""
        return 'DictionaryEmitter(%r)' % (self._items,)


class ListEmitter(object):
    """MessagePack list emitter."""

    pass
