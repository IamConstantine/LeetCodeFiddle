from typing import List


# https://leetcode.com/problems/remove-covered-intervals
# Medium
# T = O(NlogN)
# S = O(N) - as python uses timsort

def removeCoveredIntervals(intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: (x[0], -x[1]))

    count = 0

    prev = 0

    for start, end in intervals:
        if end > prev:
            count += 1
            prev = end

    return count
