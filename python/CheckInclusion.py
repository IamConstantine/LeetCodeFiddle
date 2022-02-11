from collections import Counter


# https://leetcode.com/problems/permutation-in-string
# Medium
# T = O(N)
# S = O(1) - as the worst case is 26 char hashmap

def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    counter_s1 = Counter(s1)
    length_s1 = len(s1)

    # alternate variant
    # for i in range(len(s2)):
    #     if s2[i] in counter_s1:
    #         counter_s1[s2[i]] -= 1
    #
    #     if i >= length_s1 and s2[i - length_s1] in counter_s1:
    #         counter_s1[s2[i - length_s1]] += 1
    #
    #     if all(not counter_s1[k] for k in counter_s1.keys()):
    #         return True

    curr = Counter()
    for i in range(len(s2)):
        if s2[i] in counter_s1:  # add match
            curr[s2[i]] += 1

        if i >= length_s1 and s2[i - length_s1] in counter_s1:  # get rid of out of window char
            curr[s2[i - length_s1]] -= 1

        if counter_s1 == curr:
            return True

    return False
