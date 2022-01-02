from unittest import TestCase

from Tree import createBinaryTreeFrom, toTreeArray
from TreeSerialiazer import Codec


class TestCodec(TestCase):
    def test_serialize(self):
        codec = Codec()

        serialized = codec.serialize(createBinaryTreeFrom([2, 1, 3]))
        self.assertEqual('1 3 2', serialized)
        self.assertEqual([2, 1, 3], toTreeArray(codec.deserialize(serialized)))

        serialized = codec.serialize(createBinaryTreeFrom([]))
        self.assertEqual('', serialized)
        self.assertEqual([], toTreeArray(codec.deserialize(serialized)))
