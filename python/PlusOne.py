from typing import List


def plusOne(digits: List[int]) -> List[int]:
    j = len(digits) - 1

    while j >= 0 :
        if digits[j] == 9:
            digits[j] = 0
        else:
            digits[j] += 1
            return digits
        j -= 1

    digits.insert(0, 1)
    return digits
