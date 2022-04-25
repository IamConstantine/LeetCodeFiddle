from typing import List


# https://leetcode.com/problems/count-lattice-points-inside-a-circle
# Medium

# T - O(NRR)
# S - O(XY)

# use the distance formula to check if a point is within the accepted distance ie. radius of the centre of the circle
# distance formula -> r**2>= (x2-x1)**2+(y2-y1)**2
# We use a set to deduplicate valid points generated from overlapping circles

def countLatticePoints(circles: List[List[int]]) -> int:
    return len({(x2, y2) for x1, y1, r in circles for x2 in range(x1 - r, x1 + r + 1) for y2 in
                range(y1 - r, y1 + r + 1) if (x2 - x1) ** 2 + (y2 - y1) ** 2 <= r ** 2})


# the above solution can be further optimized, if we consider the constraints.
# T = O(NXY)
# S = O(1)

# unfortunately, this times out on LC

def countLatticePoints_bounded(circles: List[List[int]]) -> int:
    cnt = 0
    for x2 in range(0, 201):
        for y2 in range(0, 201):
            for x1, y1, r in circles:
                if (x2 - x1) ** 2 + (y2 - y1) ** 2 <= r ** 2:
                    cnt += 1
                    break

    return cnt