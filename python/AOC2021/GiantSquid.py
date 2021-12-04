# AOC 4th Dec 2021
# https://adventofcode.com/2021/day/4
# Simple problem solved using a bit matrix to store marked cells on all boards
# after each number marking, check row and column of each board to check if it wins

# first half
def giantSquid():
    boards = []
    numbers = []
    with open('./inputs/GiantSquid') as f:
        numbers = [int(i) for i in f.readline().strip().split(',')]

        while f.readline():
            board = []
            for i in range(5):
                board.append([int(i.strip()) for i in (f.readline().strip().split())])
            boards.append(board)

    F = []
    for b in boards:
        F.append([[False for _ in range(5)] for _ in range(5)])

    for num in numbers:
        for i, b in enumerate(boards):
            for r in range(5):
                for c in range(5):
                    if b[r][c] == num:
                        F[i][r][c] = True

            won = False
            for r in range(5):
                ok = True
                for c in range(5):
                    if not F[i][r][c]:
                        ok = False
                        break
                if ok:
                    won = True
                    break

            for c in range(5):
                ok = True
                for r in range(5):
                    if not F[i][r][c]:
                        ok = False
                        break
                if ok:
                    won = True
                    break

            if won:
                unmarked = 0
                for r in range(5):
                    for c in range(5):
                        if not F[i][r][c]:
                            unmarked += b[r][c]

                return unmarked * num


print(giantSquid())


# 2nd Half
def giantSquidLoser():
    boards = []
    numbers = []
    with open('./inputs/GiantSquid') as f:
        numbers = [int(i) for i in f.readline().strip().split(',')]

        while f.readline():
            board = []
            for i in range(5):
                board.append([int(i.strip()) for i in (f.readline().strip().split())])
            boards.append(board)

    F = []
    for b in boards:
        F.append([[False for _ in range(5)] for _ in range(5)])

    noOfBoards = len(boards)
    wonBoards = set()
    for num in numbers:
        for i, b in enumerate(boards):
            for r in range(5):
                for c in range(5):
                    if b[r][c] == num:
                        F[i][r][c] = True

            won = False
            for r in range(5):
                ok = True
                for c in range(5):
                    if not F[i][r][c]:
                        ok = False
                        break
                if ok:
                    won = True
                    break

            for c in range(5):
                ok = True
                for r in range(5):
                    if not F[i][r][c]:
                        ok = False
                        break
                if ok:
                    won = True
                    break

            if won:
                wonBoards.add(i)
                if len(wonBoards) == noOfBoards:
                    unmarked = 0
                    for r in range(5):
                        for c in range(5):
                            if not F[i][r][c]:
                                unmarked += b[r][c]

                    return unmarked * num


print(giantSquidLoser())
