def makeStringSorted(s: str) -> int:
    input = list(s)
    length = len(input)
    sorted = False
    operations = 0
    while not sorted:
        i = length - 1
        while i != 0 and input[i] > input[i - 1]:
            i -= 1
        if i == 0:
            return operations
        j = i
        while j < length - 1 and input[i - 1] > input[j + 1]:
            j += 1

        temp = input[i - 1]
        input[i - 1] = input[j]
        input[j] = temp

        j = length - 1
        while i < j:
            temp = input[i]
            input[i] = input[j]
            input[j] = temp
            i += 1
            j -= 1
        operations += 1
