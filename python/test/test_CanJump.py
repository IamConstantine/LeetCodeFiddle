from unittest import TestCase

from CanJump import canJump, canJumpDP


class Test(TestCase):
    def test_can_jump(self):
        self.assertEqual(True, canJumpDP([2, 3, 1, 1, 4]))
        self.assertEqual(False, canJumpDP([3, 2, 1, 0, 4]))
        self.assertEqual(True, canJumpDP([1, 2, 3]))
