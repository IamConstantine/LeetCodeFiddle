from typing import List


# https://leetcode.com/problems/course-schedule
# Medium
# T = O(V + E)
# S = O(V + E)

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    adj_list = {i: [] for i in range(numCourses)}
    for x, y in prerequisites:
        adj_list[x].append(y)

    visited = set()

    def dfs(node):
        if node in visited:
            return False

        if adj_list[node] == []:
            return True

        visited.add(node)
        for x in adj_list[node]:
            if x in visited:
                return False
            dfs(x)
        adj_list[node] = []  # to mark this node is in the path of optimal solution
        visited.remove(node)
        return True

    for c in range(numCourses):  # to address disconnected graph
        if not dfs(c):
            return False

    return True
