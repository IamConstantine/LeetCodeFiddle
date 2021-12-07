# AOC 7th Dec 2021
# https://adventofcode.com/2021/day/7


import collections
import sys


# 1st half
# first solution was brute force
# Then found that the sum using median is the minimun one

def treacheryOfWhales():
    l = []
    with open('./inputs/TreacheryOfWhales') as f:
        l = list(map(int, f.readline().strip().split(',')))

    def findMedian(l):
        l.sort()
        if len(l) % 2 == 0:
            return (l[len(l) // 2] + l[(len(l) - 1) // 2]) // 2
        else:
            return l[len(l) // 2]

    med = findMedian(l)

    return sum(abs(x - med) for x in l)

    # brute force
    # positions = collections.defaultdict(int)
    # with open('./inputs/TreacheryOfWhales') as f:
    #     for i in f.readline().strip().split(','):
    #         # positions[int(i)] += 1

    # cheap = sys.maxsize
    # for i in sorted(set(positions.keys())):
    #     sumOf = 0
    #     for k, v in positions.items():
    #         sumOf += (abs(k - i) * v)
    #     cheap = min(cheap, sumOf)
    #
    # return cheap


assert (treacheryOfWhales() == 349812)


# 2nd half
def treacheryOfWhalesGeometricProgression():
    positions = collections.defaultdict(int)
    with open('./inputs/TreacheryOfWhales') as f:
        for i in f.readline().strip().split(','):
            positions[int(i)] += 1

    cheap = sys.maxsize
    for i in range(min(positions.keys()), max(positions.keys()) + 1):
        sumOf = 0
        for k, v in positions.items():
            displacement = abs(k - i)
            sumOf += (((displacement * (displacement + 1)) // 2) * v)
        cheap = min(cheap, sumOf)

    return cheap


assert (treacheryOfWhalesGeometricProgression() == 99763899)
