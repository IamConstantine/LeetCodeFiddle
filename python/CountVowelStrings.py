def countVowelStrings(n: int) -> int:
    vowels = ['a', 'e', 'i', 'o', 'u']

    def countVowelStringsInner(i):
        if i == n:
            return 0

        for ch in vowels:
            countVowelStringsInner(i + 1)

    return countVowelStringsInner(0)
