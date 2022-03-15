from collections import defaultdict
from typing import List


# https://leetcode.com/problems/campus-bikes
# Medium
# T = O(NM + K) - NM for finding pairs and K is max manhattan distance
# T = O(NM) - NM for storing pairs

def assignBikes(workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
    dist_pairs = defaultdict(list)
    min_dist = float('inf')

    # this will maintain the ordering of bikes and workers. So you dont need a sorting on these keys
    for bike_idx, bike in enumerate(bikes):
        for worker_idx, worker in enumerate(workers):
            curr_dist = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
            # bucketing
            dist_pairs[curr_dist].append((worker_idx, bike_idx))
            min_dist = min(min_dist, curr_dist)

    res = [-1] * len(workers)
    bike_status = [False] * len(bikes)

    i = 0

    curr_dist = min_dist
    while i < len(workers):

        for worker, bike in dist_pairs[curr_dist]:
            if res[worker] == -1 and not bike_status[bike]:
                res[worker] = bike
                bike_status[bike] = True
                i += 1  # increment once bike is alloted to a worker

        curr_dist += 1  # will inc to max manhattan dist ie K

    return res
