from typing import List


def maxArea(height: List[int]) -> int:
    """The intuition behind this approach is that the area formed between the lines will always be limited by
    the height of the shorter line. Further, the farther the lines, the more will be the area obtained.

    We take two pointers, one at the beginning and one at the end of the array constituting the length of the lines.
    Futher, we maintain a variable \text{maxarea}maxarea to store the maximum area obtained till now. At every step,
    we find out the area formed between them, update max_area and move the pointer pointing to the shorter
    line towards the other end by one step."""
    i = 0
    j = len(height) - 1
    max_area = -1
    while i < j:
        area = min(height[i], height[j]) * (j - i)
        max_area = max(area, max_area)

        if height[i] < height[j]:
            i += 1
        elif height[i] > height[j]:
            j -= 1
        else:
            i += 1
            j -= 1

    return max_area
