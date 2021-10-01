from unittest import TestCase

from ReverseInteger import reverse


class Test(TestCase):
    def test_reverse(self):
        self.assertEqual(0, reverse(0))
        self.assertEqual(-321, reverse(-123))
