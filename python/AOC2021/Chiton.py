from heapq import *

cave = [[*map(int, l.strip())] for l in open('./inputs/Chiton')]


def find(cave):
    risk = [[2 ** 31 for _ in x] for x in cave]
    risk[0][0] = 0

    todo = [(0, (0, 0))]
    while todo:
        _, (x, y) = heappop(todo)
        for a, b in neighbours(cave, x, y):
            if risk[a][b] > cave[a][b] + risk[x][y]:
                risk[a][b] = cave[a][b] + risk[x][y]
                heappush(todo, (risk[a][b], (a, b)))
    return risk[-1][-1]


def neighbours(cave, x, y):
    X, Y = len(cave), len(cave[0])
    for a, b in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
        if 0 <= a < X and 0 <= b < Y: yield a, b


def extend(cave):
    X, Y = len(cave), len(cave[0])
    return [[(cave[x % X][y % Y] + x // X + y // Y - 1) % 9 + 1  # logic to calculate the the x and y offset of the
             # current tile from 0th one. -1 inside is for doing the  % 9 outside first before increment. If there was no reset, we dont need the -1 + 1 logic
             for y in range(5 * Y)] for x in range(5 * X)]


print(find(cave), find(extend(cave)))
