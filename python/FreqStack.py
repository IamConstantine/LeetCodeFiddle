import heapq
from collections import Counter, defaultdict


# https://leetcode.com/problems/maximum-frequency-stack
# Hard
# T = O(log N) - for insert and delete-root
# S = O(N)

class FreqStackWithMaxHeap:

    def __init__(self):
        self.counter = Counter()
        self.heap = []
        self.idx = 0

    def push(self, val: int) -> None:
        self.counter[val] += 1
        heapq.heappush(self.heap, (-self.counter[val], -self.idx, val))
        self.idx += 1

    def pop(self) -> int:
        val = heapq.heappop(self.heap)[2]
        self.counter[val] -= 1
        if not self.counter[val]:
            del self.counter[val]
        return val


class FreqStack:

    def __init__(self):
        self.freq = Counter()
        self.group = defaultdict(list)  # grouped by freq
        self.max = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.group[self.freq[val]].append(val)
        self.max = max(self.max, self.freq[val])

    def pop(self) -> int:
        val = self.group[self.max].pop()
        self.freq[val] -= 1

        # if the max group became empty:
        # else there are other elements in that freq so don't touch
        if not self.group[self.max]:
            # this makes sense as we will always go in order and same
            # val would be in all group from 1 to max
            self.max -= 1

        return val


# Your FreqStack object will be instantiated and called as such:
obj = FreqStack()
obj.push(5)
obj.push(7)
obj.push(5)
obj.push(7)
obj.push(4)
obj.push(5)
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
