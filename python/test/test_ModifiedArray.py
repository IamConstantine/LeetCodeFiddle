from unittest import TestCase

from ModifiedArray import getModifiedArray


class Test(TestCase):
    def test_get_modified_array(self):
        self.assertEqual([-2, 0, 3, 5, 3], getModifiedArray(5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]]))
