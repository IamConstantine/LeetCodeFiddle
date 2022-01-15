from unittest import TestCase

from CourseSchedule import canFinish


class Test(TestCase):
    def test_can_finish(self):
        self.assertEqual(True, canFinish(2, [[1, 0]]))
        self.assertEqual(False, canFinish(2, [[1, 0], [0, 1]]))
