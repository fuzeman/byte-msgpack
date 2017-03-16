from __future__ import absolute_import, division, print_function

from byte.compilers.core.base import CompilerPlugin


class MessagePackCompiler(CompilerPlugin):
    key = 'msgpack'

    class Meta(CompilerPlugin.Meta):
        content_type = 'application/x-msgpack'

        extension = [
            'mpack',
            'messagepack'
        ]
