[![Build Status](https://travis-ci.org/IamConstantine/LeetCodeFiddle.svg?branch=master)](https://travis-ci.org/IamConstantine/LeetCodeFiddle)
# LeetCodeFiddle
Solutions to LeetCode problems in Scala


## Hints:

#### **Dynamic Programming**

1. [Unique Paths](https://leetcode.com/problems/unique-paths) - Use the dp array to solve this in O(mn) complexity. Instantiate first row and first column with 1 as its a known valid path to m.n. There's an intuitive recursive + memoisation solution as well.
2. [[String Two Digit Decoding](https://leetcode.com/problems/decode-ways) - The DP array solution. Each non zero is a 1 ie dp[i] = dp[i-1] and each two digits >=10 is dp[i] += dp[i-2].

#### **Divide and Conquer**

1. [Search in Rotated Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) - Use Binary search approach to solve in O(log n). Find the mid and check if right is sorted first ie compare l and mid. Binary search is called a _decrease and conquer_ problem instead of _divide and conquer_.


#### **Backtracking**

1. [Combination Sum](https://leetcode.com/problems/combination-sum) - Find all combinations for the given sum. Nothing to memoise here. You can use one node multiple times in the path to find the combination. But you cannot use your parent node once you have gone down the level.
2. [Word Search](https://leetcode.com/problems/word-search) - Intuitive solution using visited matrix and traverse all 3 directions from one cell approach.

#### **Strings**

1. [Group Anagrams](https://leetcode.com/problems/group-anagrams) - can define group key using sorted strings(O(NKlogK)) or character count(0(NK)) approach
2. [String Minimum Window](https://leetcode.com/problems/minimum-window-substring) - use length of t and l and r ptrs for window to solve this in O(2S)


#### **Array**

1. [Spiral Order](https://leetcode.com/problems/spiral-matrix) - Simple problem - The time spent is to figure out the boundaries, and edge cases(when right = left or up = down).
2. [Merge Intervals](https://leetcode.com/problems/merge-intervals) - Sort the intervals in nlogn and then just do a linear comparison.
3. [Insert Interval](https://leetcode.com/problems/insert-interval) - As the list is already sorted and has non overlapping intervals, its an easy problem which is similar to Merge Intervals
4. [Set Zeroes](https://leetcode.com/problems/set-matrix-zeroes) - Intuitive solution using additional set for row and column indices is easy. The no additional space solution is a bit tricky and read the code comments to understand that. 

#### **Greedy**

1. [Can Jump](https://leetcode.com/problems/jump-game) - Simple bottom up solution using Greedy. Just use the lastPos pointer to solve the local optima. This problem can be solved using DP as well but the solution is worse ie O(n^2)

#### **Tree**

1. [Same Tree](https://leetcode.com/problems/same-tree) - Simple preorder traversal and equality check
