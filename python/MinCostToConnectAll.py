# https://leetcode.com/problems/min-cost-to-connect-all-points
# Medium

# Kruskal's Algorithm
import heapq
from typing import List


class UnionFind:
    def __init__(self, size):
        self.group = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, node):
        if self.group[node] != node:
            self.group[node] = self.find(self.group[node])
        return self.group[node]

    def join(self, node1, node2):
        group1 = self.find(self.group[node1])
        group2 = self.find(self.group[node2])

        if group1 == group2:
            return False

        if self.rank[group1] > self.rank[group2]:
            self.group[group2] = group1
        elif self.rank[group1] < self.rank[group2]:
            self.group[group1] = group2
        else:
            self.group[group1] = group2
            self.rank[group2] += 1

        return True


# T = O(N ** 2 * log(N)) - N**2 for finding all edges and N**2 * logN for union find by rank
# S = O(N**2) - store all edges

class Kruskal:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Kruskal's MST

        n = len(points)

        # find all edges
        all_edges = []
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + \
                       abs(points[i][1] - points[j][1])
                all_edges.append((dist, i, j))

        all_edges.sort()
        uf = UnionFind(n)
        edges_added = 0
        cost = 0
        # perform union find by rank
        for weight, node1, node2 in all_edges:
            if uf.join(node1, node2):
                edges_added += 1
                cost += weight
                if edges_added == n - 1:
                    break

        return cost


class Prims:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        heap = [(0, 0)]

        visited = [False] * n
        edges_used = 0
        cost = 0

        while edges_used < n:
            weight, curr_node = heapq.heappop(heap)

            if visited[curr_node]:
                continue
            visited[curr_node] = True
            edges_used += 1
            cost += weight

            for next_node in range(n):
                if not visited[next_node]:
                    weight = abs(points[curr_node][0] - points[next_node][0]) + \
                             abs(points[curr_node][1] - points[next_node][1])

                    heapq.heappush(heap, (weight, next_node))

        return cost


# T = O(N**2)
# S = O(N)

class PrimsOptimized:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        edges_used = 0
        cost = 0
        visited = [False] * n

        # initialize cost of each node in graph.
        # Each node will be updated with min weight required to hop to adjacent node
        min_dist = [float('inf')] * n
        min_dist[0] = 0

        while edges_used < n:
            curr_node = -1
            min_edge = float('inf')

            for i in range(n):
                if not visited[i] and min_dist[i] < min_edge:
                    min_edge = min_dist[i]
                    curr_node = i

            visited[curr_node] = True
            edges_used += 1
            cost += min_edge

            # update cost of all adjacent vertices
            for next_node in range(n):
                weight = abs(points[curr_node][0] - points[next_node][0]) + \
                         abs(points[curr_node][1] - points[next_node][1])

                if not visited[next_node] and weight < min_dist[next_node]:
                    min_dist[next_node] = weight

        return cost
