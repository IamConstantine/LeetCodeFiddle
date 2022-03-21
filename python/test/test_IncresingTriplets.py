from unittest import TestCase

from IncresingTriplets import increasingTriplet


class Test(TestCase):
    def test_increasing_triplet(self):
        self.assertEqual(True, increasingTriplet([1, 2, 3, 4, 5]))
        self.assertEqual(False, increasingTriplet([5, 4, 3, 2, 1]))
        self.assertEqual(True, increasingTriplet([2, 1, 5, 0, 4, 6]))
