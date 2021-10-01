from unittest import TestCase

from Candy import candy


class Test(TestCase):
    def test_candy(self):
        self.assertEqual(5, candy([1, 0, 2]))
        self.assertEqual(13, candy([1,2,87,87,87,2,1]))
        self.assertEqual(18, candy([1,6,10,8,7,3,2]))
        self.assertEqual(12, candy([29,51,87,87,72,12]))

