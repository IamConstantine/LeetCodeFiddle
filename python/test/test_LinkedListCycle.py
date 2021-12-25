from unittest import TestCase

from LinkedListCycle import hasCycle
from ListNode import createLL_with_cycle


class Test(TestCase):
    def test_has_cycle(self):
        self.assertEqual(True, hasCycle(createLL_with_cycle([3, 2, 0, -4], 1)))
        self.assertEqual(True, hasCycle(createLL_with_cycle([1, 2], 0)))
        self.assertEqual(False, hasCycle(createLL_with_cycle([1], -1)))
        self.assertEqual(False, hasCycle(createLL_with_cycle([], -1)))
