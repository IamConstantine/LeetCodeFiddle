def dumoOctopus():
    octopus = {}
    with open('./inputs/DumoOctopus') as f:
        octopus = {
            (r, c): value for r, line in enumerate(f.readlines()) for c, value in enumerate(line.strip())
        }

    def findNeighbours(x, y):
        return filter(lambda x: x in octopus and octopus[x][y] <= 9,
                      [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1), (x - 1, y - 1), (x + 1, y + 1), (x - 1, y + 1),
                       (x + 1, y - 1)])

    def startFlash(p):

    for k in octopus.keys():
        octopus[k] += 1

    for k in octopus.keys():
        if octopus[k] > 9:
            flashed = [k]
            neighbours = findNeighbours(*k)
            for p in neighbours:
                octopus[p] += 1

            flashed += filter(lambda x: x >9 , neighbours)
            for flash in flashed:

print(dumoOctopus())
