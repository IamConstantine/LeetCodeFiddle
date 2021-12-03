# AOC 3rd Dec 2021
# https://adventofcode.com/2021/day/3
# 1st half
def calculateDiagnosis():
    cnt = [
        [0, 0]
        , [0, 0]
        , [0, 0]
        , [0, 0]
        , [0, 0]
        , [0, 0]
        , [0, 0]
        , [0, 0]
        , [0, 0]
        , [0, 0]
        , [0, 0]
        , [0, 0]
    ]
    with open("./inputs/CalculateDiagnosis") as f:
        for line in f:
            for i, c in enumerate(line.strip()):
                cnt[i][int(c)] += 1
    exp = 11
    gamma = 0
    epsilon = 0
    for pos in cnt:
        if pos[1] > pos[0]:
            gamma += 2 ** exp
        else:
            epsilon += 2 ** exp
        exp -= 1

    return gamma * epsilon


print(calculateDiagnosis())


# 2nd half

def calculateHealthRating():
    numbers = []
    with open("./inputs/CalculateDiagnosis") as f:
        for line in f:
            numbers.append(line.strip())

    valid_o2 = numbers
    valid_co2 = numbers
    for i in range(12):
        if len(valid_o2) > 1:
            part = [[], []]
            for num in valid_o2:
                part[int(num[i])].append(num)

            if len(part[0]) > len(part[1]):
                valid_o2 = part[0]
            else:
                valid_o2 = part[1]

        if len(valid_co2) > 1:
            part = [[], []]
            for num in valid_co2:
                part[int(num[i])].append(num)

            if len(part[1]) < len(part[0]):
                valid_co2 = part[1]
            else:
                valid_co2 = part[0]

    o2 = int(valid_o2[0], 2)
    co2 = int(valid_co2[0], 2)
    return o2 * co2


print(calculateHealthRating())
