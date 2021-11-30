import collections
from typing import List


# https://leetcode.com/problems/group-anagrams
# Medium
# Using Sorted String
# Time Complexity: O(NKlog K), where N is the length of strs, and K is the maximum length of a string in strs. The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(Klog K) time.
# Space Complexity: O(NK), the total information content stored in ans
#

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # m = {}
    #
    # for x in strs:
    #     sortedStr = ''.join(sorted(x))
    #     m[sortedStr] = m.get(sortedStr) + [x]  if m.get(sortedStr) else [x]
    #
    # return list(m.values())

    m = collections.defaultdict(list)  # this will not need the None like I did for dict and also this is mutable dict

    for x in strs:
        m[tuple(sorted(x))].append(x)

    return list(m.values())


# Using Character count: Best
# Time Complexity: O(NK), where N is the length of strs, and K is the maximum length of a string in strs. Counting each string is linear in the size of the string, and we count every string.
# Space Complexity: O(NK), the total information content stored in ans.

# On paper, this is faster but time and space requirements were more for this solution. Dont know why though
def groupAnagramsBest(strs: List[str]) -> List[List[str]]:
    m = collections.defaultdict(list)

    for x in strs:
        # can try using dict but the issue is generating a hash to be the key for strs
        # so prefer to do using alphabet array
        cnt = [0] * 26

        for c in x:
            cnt[ord(c) - ord('a')] += 1  # as we are only dealing with lowercase chars

        m[tuple(cnt)].append(x)
    return list(m.values())