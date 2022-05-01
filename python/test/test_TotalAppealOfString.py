from unittest import TestCase

from TotalAppealOfString import appealSum


class Test(TestCase):
    def test_appeal_sum(self):
        self.assertEqual(28, appealSum('abbca'))
        self.assertEqual(20, appealSum('code'))
        self.assertEqual(18, appealSum('fxfz'))
