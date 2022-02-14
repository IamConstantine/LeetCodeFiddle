from typing import List


# https://leetcode.com/problems/alien-dictionary
# Hard
# T = O(C) - total no of chars from all words : C
# S = O(U + min(U^2, N)) - N: no of words and U: unique chars

def alienOrder(words: List[str]) -> str:
    reversed_adj_list = {c: [] for word in words for c in word}  # O(C)

    # build a reverse adjacency list to start traversal from non indegree nodes to zero indegree nodes
    # This is required for topological sort

    for first, second in zip(words, words[1:]):  # O(U + min(U^2, N)) and its < O(C)
        for f, s in zip(first, second):
            if f != s:
                reversed_adj_list[s].append(f)
                break
        else:
            if len(second) < len(first):
                return ''

    seen = {}
    output = []

    # dfs
    def visit(node):
        if node in seen:
            return seen[node]

        seen[node] = False

        for adj in reversed_adj_list[node]:
            if not visit(adj):
                return False

        seen[node] = True
        output.append(node)

        return True

    if not all(visit(x) for x in reversed_adj_list):  # traverse through each for topological sort
        return ''

    return ''.join(output)
