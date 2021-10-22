from typing import List, Optional

from Tree import TreeNode


def allPossibleFBT(n: int) -> List[Optional[TreeNode]]:
    mem = {0: [], 1: [TreeNode(0)]}

    def allPossibleFBTInner(N) -> List[Optional[TreeNode]]:
        if N in mem:
            return mem[N]

        ans = []
        for x in range(N):
            y = N - 1 - x
            for left in allPossibleFBTInner(x):
                for right in allPossibleFBTInner(y):
                    bns = TreeNode(0)
                    bns.left = left
                    bns.right = right
                    ans.append(bns)

        mem[N] = ans
        return ans

    return allPossibleFBTInner(n)
