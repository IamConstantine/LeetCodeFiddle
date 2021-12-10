from collections import Counter


# AOC 10th Dec 2021
# https://adventofcode.com/2021/day/10

# Part 1
def syntaxScoringCorruptedLines():
    openAndScore = {
        ')': ('(', 3),
        ']': ('[', 57),
        '}': ('{', 1197),
        '>': ('<', 25137)
    }

    valid_set = set(map(lambda x: x[0], openAndScore.values()))
    counter = Counter()

    with open('./inputs/SyntaxScoring') as f:
        for line in f.readlines():
            stack = []
            for c in line.strip():
                if c in valid_set:
                    stack.append(c)
                else:
                    if stack:
                        popped = stack.pop()
                        if openAndScore[c][0] != popped:
                            counter[c] += 1
                            break
    return sum(openAndScore[k][1] * v for k, v in counter.items())


assert (syntaxScoringCorruptedLines() == 339411)

# Part 2

def syntaxScoringIncompleteLines():
    pairs = {
        '(': (')', 1),
        '[': (']', 2),
        '{': ('}', 3),
        '<': ('>', 4)
    }

    scores = []
    with open('./inputs/SyntaxScoring') as f:
        for line in f.readlines():
            stack = []  # clean slate after every line
            corrupted = False
            for c in line.strip():
                if c in pairs:
                    stack.append(c)
                else:
                    if stack:
                        popped = stack.pop()
                        if pairs[popped][0] != c:
                            corrupted = True
                            break  # if corrupted break



            if stack and not corrupted:  # incomplete lines
                total = 0
                for x in reversed(stack):
                    total = (5 * total) + pairs[x][1]
                scores.append(total)

    scores.sort()
    mid = len(scores) // 2
    return scores[mid]


assert (syntaxScoringIncompleteLines() == 2289754624)
