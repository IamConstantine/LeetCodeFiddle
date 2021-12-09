# AOC 9th Dec 2021
# https://adventofcode.com/2021/day/9

# I had solved it using another approach which was more verbose and had more LOC
# Then I found a brilliant solution on reddit with some python contructs which I hadnt seen before.
# Updating the codebase with that solution for reference and I also removed my code as it was ugly infront of this beauty

# part 1
from math import prod

height = {}
with open('./inputs/SmokeBasin') as f:
    height = {(x, y): int(h)
              for y, l in enumerate(f.readlines())
              for x, h in enumerate(l.strip())
              }


def neighbours(x, y):
    return filter(lambda n: n in height, [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)])


def is_low(p):
    return all(height[p] < height[x] for x in neighbours(*p))


low_points = [*filter(is_low, height)]

assert (sum(height[p] + 1 for p in low_points) == 486)


# part 2
def count_basin(p):
    if height[p] == 9:
        return 0
    del height[p]  # no need for visited array then
    return 1 + sum(count_basin(n) for n in neighbours(*p))  # include the current one


basins = [count_basin(p) for p in low_points]  # count of each basin

print(prod(sorted(basins)[-3:]))  # pick last 3
