# AOC 1st Dec 2021

# 1st half
def finalPosition():
    depth = 0
    horizontal = 0
    with open('./inputs/FinalPosition') as f:
        for line in f:
            direction = line.split(' ')[0][0]
            value = int(line.split(' ')[1])
            if direction == 'f':
                horizontal += value
            elif direction == 'd':
                depth += value
            elif direction == 'u':
                depth -= value

    return depth * horizontal


print(finalPosition())


# 2nd half
def finalPositionWithAim():
    depth = 0
    horizontal = 0
    aim = 0
    with open('./inputs/FinalPosition') as f:
        for line in f:
            direction = line.split(' ')[0][0]
            value = int(line.split(' ')[1])
            if direction == 'f':
                horizontal += value
                depth += aim * value
            elif direction == 'd':
                aim += value
            elif direction == 'u':
                aim -= value

    return depth * horizontal


print(finalPositionWithAim())
