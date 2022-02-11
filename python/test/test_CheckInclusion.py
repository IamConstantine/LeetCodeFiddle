from unittest import TestCase

from CheckInclusion import checkInclusion


class Test(TestCase):
    def test_check_inclusion(self):
        self.assertEqual(True, checkInclusion('ab', 'eidbaooo'))
        self.assertEqual(False, checkInclusion('ab', 'eidboaoo'))
