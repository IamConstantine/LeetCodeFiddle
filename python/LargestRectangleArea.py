from typing import List


# https://leetcode.com/problems/largest-rectangle-in-histogram
# Hard
# T = O(NlogN) - Divide and Conquer - would be worse O(n**2) if array is sorted
# S = O(N)

def largestRectangleArea_divideAndConquer(heights: List[int]) -> int:
    def largestRectangleAreaInner(start, end):
        if start == end:
            return heights[start]
        if start > end:
            return 0

        min_index = start
        for i in range(start + 1, end + 1):
            if heights[i] < heights[min_index]:
                min_index = i

        return max(heights[min_index] * (end - start + 1), largestRectangleAreaInner(start, min_index - 1),
                   largestRectangleAreaInner(min_index + 1, end))

    return largestRectangleAreaInner(0, len(heights) - 1)


# T = O(N)
# S = O(N)

def largestRectangleArea(heights: List[int]) -> int:
    stack = [-1]  # this would act as special case when stack is empty and we want a width 1
    max_area = 0
    for i in range(len(heights)):
        while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
            height = heights[stack.pop()]
            width = i - stack[-1] - 1  # need to subtract from top of stack which is used calculate distance to i
            max_area = max(max_area, height * width)
        stack.append(i)

    # pop out remaining stack
    while stack[-1] != -1:
        height = heights[stack.pop()]
        width = len(heights) - stack[-1] - 1
        max_area = max(max_area, height * width)
    return max_area
