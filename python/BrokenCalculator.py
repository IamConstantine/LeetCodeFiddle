# https://leetcode.com/problems/broken-calculator
# Medium
# T = O(log target)
# S = O(1)

# If with subtraction and multiplication, the effect of earlier subtraction will be amplified by later
# multiplications, hence, greedily doing multiplication might not reach optimal solution as an additional early
# subtraction can have a huge effect. Whereas with addition and division, earlier addition will be diminished by
# later divisions. It is thus always better to do division wherever possible.

def brokenCalc(startValue: int, target: int) -> int:
    ans = 0

    while target > startValue:
        ans += 1

        if target % 2:
            target += 1  # make it even
        else:
            target //= 2  # greedily subtract to make target smaller

    return ans + startValue - target  # add the steps remaining from target tp startValue
