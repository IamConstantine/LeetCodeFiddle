from unittest import TestCase

from ValidateStackSequences import validateStackSequences


class Test(TestCase):
    def test_validate_stack_sequences(self):
        self.assertTrue(validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
        self.assertFalse(validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
