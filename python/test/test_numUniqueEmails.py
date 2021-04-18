from unittest import TestCase

from NumUniqueEmails import numUniqueEmails


class TestSolution(TestCase):
    def test_num_unique_emails(self):
       self.assertEqual (2, numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))

