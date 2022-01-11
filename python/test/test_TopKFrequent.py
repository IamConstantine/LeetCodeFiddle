from unittest import TestCase

from TopKFrequent import topKFrequent


class Test(TestCase):
    def test_top_kfrequent(self):
        self.assertCountEqual([1, 2], topKFrequent([1, 1, 1, 2, 2, 3], 2))
        self.assertCountEqual([1], topKFrequent([1], 1))
