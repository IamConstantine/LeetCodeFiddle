import heapq
from typing import List


# https://leetcode.com/problems/meeting-rooms-ii
# Medium


# T = O(NLogN) - using Heap
# S = O(N)

def minMeetingRooms_Heap(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0

    rooms = []

    intervals.sort(key=lambda x: x[0])

    heapq.heappush(rooms, intervals[0][1])

    for start, end in intervals[1:]:
        if rooms[0] <= start:
            heapq.heappop(rooms)

        heapq.heappush(rooms, end)
    return len(rooms)


# T = O(NLogN) - Chronological ordering
# S = O(N)

def minMeetingRooms(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0

    start_ts = sorted(x[0] for x in intervals)
    end_ts = sorted(x[1] for x in intervals)

    rooms = 0
    start_ptr = 0
    end_ptr = 0

    while start_ptr < len(intervals):
        if start_ts[start_ptr] >= end_ts[end_ptr]:
            rooms -= 1
            end_ptr += 1

        rooms += 1
        start_ptr += 1

    return rooms
