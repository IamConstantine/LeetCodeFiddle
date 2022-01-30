from unittest import TestCase

from GroupShiftedStrings import groupStrings


class Test(TestCase):
    def test_group_strings(self):
        self.assertCountEqual([["acef"], ["a", "z"], ["abc", "bcd", "xyz"], ["az", "ba"]],
                              groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
