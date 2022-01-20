import heapq


# https://leetcode.com/problems/find-median-from-data-stream
# Hard
# T = O(5LogN) - addNum - worst case 3 insertions and 2 deletions per call
# T = O(1) - calculate median
# S = O(N) - no of elements added

# Two Heap Solution
# Python default heapq is minheap. So to convert it into maxheap, negate the elements when adding to maxheap.

class MedianFinder:

    def __init__(self):
        self.lo = []
        self.high = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.high, -(heapq.heappop(self.lo)))

        while len(self.lo) < len(self.high):
            heapq.heappush(self.lo, -(heapq.heappop(self.high)))

    def findMedian(self) -> float:
        return -self.lo[0] if len(self.lo) > len(self.high) else (-self.lo[0] + self.high[0]) * 0.5
