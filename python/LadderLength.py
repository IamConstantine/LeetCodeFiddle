from collections import deque
from typing import List


# https://leetcode.com/problems/word-ladder
# Hard
# T = O(M^2 * N)
# S = O(M^2 * N) - M * N = Q, Hashset and finding combo - every word has M combinations - M ^ 2 * N

def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    word_set = set(wordList)

    chars_list = [{word[i] for word in word_set} for i in range(len(beginWord))]

    if beginWord in word_set:
        word_set.remove(beginWord)
    q = deque()
    q.append(beginWord)
    level = 0

    while q:
        size = len(q)
        level += 1

        for i in range(size):  # N
            popped = q.popleft()
            if popped == endWord:
                return level

            for i in range(len(popped)):  # M
                for c in chars_list[i]:
                    new = popped[:i] + c + popped[i + 1:]  # takes M
                    if new in word_set:
                        q.append(new)
                        word_set.remove(new)

    return 0
