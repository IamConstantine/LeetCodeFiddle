# https://leetcode.com/explore/interview/card/google/66/others-4/3099/

mappings = {
    '6': '9',
    '9': '6',
    '0': '0',
    '1': '1',
    '8': '8'
}


def isStrobogrammatic(num: str) -> bool:
    len_s = len(num)

    i = 0
    j = len_s - 1
    while i <= j:
        if (num[i] not in mappings) or (num[i] in mappings and mappings[num[i]] != num[j]):
            return False
        i += 1
        j -= 1
    return True
