from typing import List


# https://leetcode.com/problems/insert-interval
# Medium

# Made a mistake here. I thought that I could merge the input interval since I just solved mergeIntervals problem
# Simply missed this statement -> You are given an array of non-overlapping intervals.......
# T = O(N) - list is already sorted
# S = O(N) - for the output

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    merged = []
    i = 0
    while i < len(intervals) and intervals[i][0] < newInterval[0]:
        merged.append(intervals[i])
        i += 1

    if not merged or merged[-1][1] < newInterval[0]:  # no overlap
        merged.append(newInterval)
    else:
        merged[-1][1] = max(merged[-1][1], newInterval[1])

    while i < len(intervals):
        if merged[-1][1] < intervals[i][0]:  # no overlap
            merged.append(intervals[i])
        else:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
        i += 1
    return merged
