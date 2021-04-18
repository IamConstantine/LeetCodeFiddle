from typing import List


def numUniqueEmails(emails: List[str]) -> int:
    unique = set()
    for email in emails:
        unique.add(normalize_email(email))
    return len(unique)


def normalize_email(email):
    (local_name, domain) = email.split('@')
    return local_name.split('+')[0].replace('.', '') + '@' + domain
