# https://leetcode.com/problems/remove-duplicate-letters
# Medium
# T = O(N)
# S = O(N)

def removeDuplicateLetters(s: str) -> str:
    stck = []
    seen = set()  # to maintain one copy of char in stck

    last_idx = {c: i for i, c in
                enumerate(s)}  # this is for finding a substring that is high in lexicographical ordering

    for i, c in enumerate(s):
        if c not in seen:

            # pop stack and remove visited for a character if its not high in ordering
            while stck and c < stck[-1] and i < last_idx[stck[-1]]:
                seen.discard(stck.pop())
            seen.add(c)
            stck.append(c)

    return ''.join(stck)
