from unittest import TestCase

from OneThreeTwoPattern import find132pattern


class Test(TestCase):
    def test_find132pattern(self):
        self.assertEqual(False, find132pattern([1, 2, 3, 4]))
        self.assertEqual(True, find132pattern([3, 1, 4, 2]))
