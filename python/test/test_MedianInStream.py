from unittest import TestCase

from MedianInStream import MedianFinder


class TestMedianFinder(TestCase):
    def test_median(self):
        obj = MedianFinder()
        obj.addNum(4)
        obj.addNum(1)
        self.assertEqual(2.5, obj.findMedian())

        obj.addNum(3)
        self.assertEqual(3, obj.findMedian())
