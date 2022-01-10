# https://leetcode.com/problems/non-overlapping-intervals/submissions/
# Medium

# T = O(nlogn)
# S = O(1)

def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[0])
    prev = intervals[0][1]
    cnt = 0
    for curr in intervals[1:]:
        if prev > curr[0]:
            prev = min(prev, curr[1])
            cnt += 1
        else:
            prev = curr[1]
    return cnt
