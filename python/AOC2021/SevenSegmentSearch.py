# AOC 8th Dec 2021
# https://adventofcode.com/2021/day/8


# part 1
def sevenSegmentSearch():
    cnt = 0
    uniqueSegmentCounts = {2, 4, 3, 7}
    with open('./inputs/SevenSegmentSearch') as f:
        for line in f.readlines():
            for output_value in line.split('|')[1].strip().split():
                cnt += (len(output_value) in uniqueSegmentCounts)
    return cnt


assert (sevenSegmentSearch() == 245)


#part 2
def sevenSegmentSearchInferDigits():
    addition = 0
    sect = lambda s, t: sum(1 for l in s if l in t)

    with open('./inputs/SevenSegmentSearch') as f:
        for line in f.readlines():
            k = line.strip().split(" | ")
            a = k[0].split(" ")
            b = k[1].split(" ")
            for c in a + b:
                if len(c) == 2: one = c
                if len(c) == 4: four = c
            s = ""
            for c in b:
                if len(c) == 2:
                    s += "1"
                elif len(c) == 3:
                    s += "7"
                elif len(c) == 4:
                    s += "4"
                elif len(c) == 7:
                    s += "8"
                elif len(c) == 5:
                    if sect(c, one) == 2:
                        s += "3"
                    elif sect(c, four) == 2:
                        s += "2"
                    else:
                        s += "5"
                else:
                    if sect(c, four) == 4:
                        s += "9"
                    elif sect(c, one) == 2:
                        s += "0"
                    else:
                        s += "6"

            addition += int(s)
    return addition


assert (sevenSegmentSearchInferDigits() == 983026)
