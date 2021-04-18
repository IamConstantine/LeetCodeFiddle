from collections import defaultdict
from typing import List


def totalFruit(tree: List[int]) -> int:
    cnt = 0
    dict = defaultdict(int)
    maxTotal = 0
    for i in range(len(tree)):
        if not dict[tree[i]] and len(dict) > 2:
            maxTotal = max(maxTotal, cnt)
            cnt = dict[tree[i-1]]
            dict = defaultdict(int, {tree[i - 1]: dict[tree[i - 1]]})
        if i > 0 and tree[i] == tree[i-1]:
            dict[tree[i]] += 1
        else:
            dict[tree[i]] = 1
        cnt += 1

    return max(maxTotal, cnt)