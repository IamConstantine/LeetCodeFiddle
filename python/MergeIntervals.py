from typing import List


# https://leetcode.com/problems/merge-intervals
# Medium

# First solution using sorting. Python uses Timsort which O(n.log n). So the problem is solved in T = O(n.log n)
# S = O(logN) for sorting

def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    merged = []
    prev = intervals[0]
    for item in intervals[1:]:
        if prev[1] >= item[0]:
            prev[1] = max(prev[1], item[1])
        else:
            merged.append(prev)
            prev = item
    merged.append(prev)
    return merged
