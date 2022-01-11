from typing import List
from collections import Counter


# https://leetcode.com/problems/top-k-frequent-elements
# Medium

# If sorting was allowed, then its pretty easy
# T = O(nlogn)
# S = O(n)

def topKFrequent_sort(nums: List[int], k: int) -> List[int]:
    counter = list(Counter(nums).items())

    counter.sort(key=lambda x: x[1])

    return list(map(lambda x: x[0], counter[-k:]))


# Quick select is used which will result in
# T = O(N) average case. If a bad pivot is selected constantly, it might result in O(N^2)


def topKFrequent(nums: List[int], k: int) -> List[int]:
    counter = Counter(nums)
    unique = list(counter.keys())

    def partition(left, right, pivot):
        pivot_freq = counter[unique[pivot]]

        # move pivot to end start partitioning
        unique[right], unique[pivot] = unique[pivot], unique[right]

        index = left
        # move all less frequent elements to the left
        for i in range(left, right):
            if counter[unique[i]] < pivot_freq:
                unique[i], unique[index] = unique[index], unique[i]
                index += 1

        # move pivot to its right place
        unique[right], unique[index] = unique[index], unique[right]
        return index

    def quick_select(left, right, kth_index):
        if left == right:
            return

        pivot_index = left  # random.randint(left, right) -> for choosing random pivot(to avoid bad pivots)

        pivot_index = partition(left, right, pivot_index)

        if kth_index == pivot_index:  # it has moved all k high frequent elements to the right of unique array
            return

        if kth_index < pivot_index:
            quick_select(left, pivot_index - 1, kth_index)
        else:
            quick_select(pivot_index + 1, right, kth_index)

    n = len(unique)
    quick_select(0, n - 1, n - k)
    return unique[-k:]
