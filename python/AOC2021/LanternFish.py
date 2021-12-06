# AOC 6th Dec 2021
# https://adventofcode.com/2021/day/6


def lanternFishInsane(days):
    input_fishes = [0] * 9
    with open('./inputs/LanternFish') as f:
        for i in f.readline().strip().split(','):
            input_fishes[int(i)] += 1

    for t in range(days):
        input_fishes[(t + 7) % 9] += input_fishes[t % 9]

    return sum(input_fishes)


def lanternFish(days):
    input_fishes = [0] * 9
    with open('./inputs/LanternFish') as f:
        for i in f.readline().strip().split(','):
            input_fishes[int(i)] += 1

    for _ in range(days):
        breed = input_fishes[0]
        for i in range(8):  # move each counts everyday up and add 0th value to 6 and 8
            input_fishes[i] = input_fishes[i + 1]
            input_fishes[i + 1] = 0
        input_fishes[6] += breed  # reset fish after breeding
        input_fishes[8] += breed  # spawn a new fish
    return sum(input_fishes)


assert (lanternFish(80) == 361169)  # part 1
assert (lanternFish(256) == 1634946868992)  # part 2
