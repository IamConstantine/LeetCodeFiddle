from typing import List


# https://leetcode.com/problems/meeting-rooms
# Easy
# T = O(NlogN)
# S = O(1)

def canAttendMeetings(intervals: List[List[int]]) -> bool:
    if len(intervals) == 0:
        return True

    intervals.sort(key=lambda x: x[0])

    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i + 1][0]:
            return False
    return True
