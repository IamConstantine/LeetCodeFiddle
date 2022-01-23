from unittest import TestCase

from StringCodec import StringCodec


class TestStringCodec(TestCase):
    def test_stringCoded(self):
        obj = StringCodec()
        expected = ["Hello", "World"]
        msg = obj.encode(expected)
        self.assertCountEqual(expected, obj.decode(msg))
