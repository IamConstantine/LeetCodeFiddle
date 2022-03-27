from unittest import TestCase

from MinDeletionsToBeautifulArray import minDeletion


class Test(TestCase):
    def test_min_deletion(self):
        self.assertEqual(1, minDeletion([1, 1, 2, 3, 5]))
        self.assertEqual(2, minDeletion([1, 1, 2, 2, 3, 3]))
