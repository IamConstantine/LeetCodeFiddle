# AOC 1st Dec 2021
import sys


# 1st half
def countIncrease():
    with open('AOC2021/inputs/CountIncrease') as f:
        prev = sys.maxsize
        cnt = 0
        for curr in f:
            if prev < int(curr):
                cnt += 1
            prev = int(curr)
    return cnt


print(countIncrease())


# 2nd half
def countIncreaseWindow():
    with open('AOC2021/inputs/CountIncrease') as f:
        prev = sys.maxsize
        cnt = 0
        l = []
        for line in f:
            l.append(int(line))

        first = l[0] + l[1] + l[2]

        for i in range(3, len(l)):
            second = first - l[i - 3] + l[i]
            if first < second:
                cnt += 1
            first = second
    return cnt


print(countIncreaseWindow())
