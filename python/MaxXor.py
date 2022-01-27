from typing import List


# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array
# Marked as Medium but its Hard

# T = O(N)
# S = O(1)
# This approach is a bit hard

def findMaximumXOR_bitManipulation(nums: List[int]) -> int:
    max_xor = 0
    mask = 0
    L = len(bin(max(nums))) - 2
    for i in range(L)[::-1]:
        mask |= 1 << i
        prefixes = {n & mask for n in nums}

        tmp = max_xor | (1 << i)
        if any(tmp ^ prefix in prefixes for prefix in prefixes):
            max_xor = tmp
    return max_xor


# T = O(N)
# S = O(2**L) = O(M) nodes of the Trie

def findMaximumXOR(nums: List[int]) -> int:
    L = len(bin(max(nums))) - 2
    # Lpad with zeros
    nums = [[(x >> i) & 1 for i in range(L)][::-1] for x in nums]  # with L = 4, 3 will be [0,0,1,1]

    # Build Bit Trie
    trie = {}
    for num in nums:
        node = trie
        for bit in num:
            if bit not in node:
                node[bit] = {}
            node = node[bit]

    # find max_xor
    max_xor = 0
    for num in nums:
        xor_node = trie
        curr_xor = 0  # tracks number which produces best trie path for current number
        for bit in num:
            # as we are trying to find best case path for current path, we will find node with opposite bit
            # as 1 ^ 0 = 1 and 1 ^ 1 = 0
            # we need to find path in trie with max xor set for current num

            toggled = 1 - bit

            if toggled in xor_node:
                curr_xor = curr_xor << 1 | 1
                xor_node = xor_node[toggled]
            else:
                curr_xor = curr_xor << 1
                xor_node = xor_node[bit]

        max_xor = max(max_xor, curr_xor)
    return max_xor
