# AOC 5th Dec 2021
# https://adventofcode.com/2021/day/5
# I had to google math equation to find all points on a line segment
# Once you get all the points, the solution is derived using a dict

import collections


def sign(x):
    return (x > 0) - (x < 0)


# first find the intervals for both x and y using x2-x1 and y2-y1
# then just keep on adding interval to x1,y1 until it equates to x2,y2
def count_overlaps(segments, include_diagonals):
    freq = collections.defaultdict(int)
    for (x1, y1), (x2, y2) in segments:
        if x1 == x2 or y1 == y2 or include_diagonals:
            x_inc, y_inc = sign(x2 - x1), sign(y2 - y1)
            while (x1, y1) != (x2 + x_inc, y2 + y_inc):
                freq[(x1, y1)] += 1
                x1 += x_inc
                y1 += y_inc
    return sum(i > 1 for i in freq.values())


def hydrothermalVenture(include_diagonals):
    segments = []
    with open("./inputs/HydrothermalVenture") as f:
        for line in f:
            point1, point2 = line.split(' -> ')
            x1, y1 = map(int, point1.split(','))
            x2, y2 = map(int, point2.split(','))
            segments.append(((x1, y1), (x2, y2)))

    return count_overlaps(segments, include_diagonals)


assert (hydrothermalVenture(False) == 5835)  # part 1
assert (hydrothermalVenture(True) == 17013)  # part2
