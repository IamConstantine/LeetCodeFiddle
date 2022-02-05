from typing import List


# https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends
# Medium
# T = O(NLogN + N + Nα(M)) - sorting + group ID array creation + amortized time for Union find
# S = O(N) - sorting, O(M) - for groups = O(N + M)

def earliestAcq(logs: List[List[int]], n: int) -> int:
    logs.sort(key=lambda x: x[0]) # Timsort

    union_find = UnionFind(n)
    group_size = n

    for ts, a, b in logs:
        if union_find.union(a, b):
            group_size -= 1

        if group_size == 1:
            return ts

    return -1


class UnionFind:
    def __init__(self, size):
        self.group = [i for i in range(size)]
        self.rank = [0] * size

    def union(self, a, b):
        root_a = self.find_root(a)
        root_b = self.find_root(b)

        if root_a == root_b:
            return False

        if self.rank[root_a] < self.rank[root_b]:
            self.group[root_a] = root_b
        elif self.rank[root_a] > self.rank[root_b]:
            self.group[root_b] = root_a
        else:
            self.group[root_a] = root_b
            self.rank[root_b] += 1

        return True

    def find_root(self, person):
        if person != self.group[person]:
            self.group[person] = self.find_root(
                self.group[person])  # updating all the members of the group while traversing to find root
        return self.group[person]
