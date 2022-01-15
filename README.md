[![Build Status](https://travis-ci.org/IamConstantine/LeetCodeFiddle.svg?branch=master)](https://travis-ci.org/IamConstantine/LeetCodeFiddle)
# LeetCodeFiddle
Solutions to LeetCode problems in Scala


## Hints:

#### **Dynamic Programming**

1. [Unique Paths](https://leetcode.com/problems/unique-paths) - Use the dp array to solve this in O(mn) complexity. Instantiate first row and first column with 1 as its a known valid path to m.n. There's an intuitive recursive + memoisation solution as well.
2. [String Two Digit Decoding](https://leetcode.com/problems/decode-ways) - The DP array solution. Each non zero is a 1 ie dp[i] = dp[i-1] and each two digits >=10 is dp[i] += dp[i-2].
3. [Word Break](https://leetcode.com/problems/word-break) - DP Recursion + memoisation
4. [House Robber](https://leetcode.com/problems/house-robber) - Calculate max(i + i-2, i-1). 
5. [Long Increasing Sequence](https://leetcode.com/problems/longest-increasing-subsequence) - An N^2 algo to compute the seq length for eveyr ith valu
6. [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence) - use
   bottom up on a dp[text1+1][text2+1] array. Refer the solution section for more details.

#### **Divide and Conquer**

1. [Search in Rotated Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) - Use Binary search approach to solve in O(log n). Find the mid and check if right is sorted first ie compare l and mid. Binary search is called a _decrease and conquer_ problem instead of _divide and conquer_.
2. [Find Min in Rotated Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array) - Use Binary Search to find min in search space.

#### **Backtracking**

1. [Combination Sum](https://leetcode.com/problems/combination-sum) - Find all combinations for the given sum. Nothing to memoise here. You can use one node multiple times in the path to find the combination. But you cannot use your parent node once you have gone down the level.
2. [Word Search](https://leetcode.com/problems/word-search) - Intuitive solution using visited matrix and traverse all 3 directions from one cell approach.

#### **Strings**

1. [Group Anagrams](https://leetcode.com/problems/group-anagrams) - can define group key using sorted strings(O(NKlogK)) or character count(0(NK)) approach
2. [String Minimum Window](https://leetcode.com/problems/minimum-window-substring) - use length of t and l and r ptrs for window to solve this in O(2S)
3. [Validate Palindrome](https://leetcode.com/problems/valid-palindrome) - Easy problem solved using a l and r pointer.
4. [Is Anagram ?](https://leetcode.com/problems/valid-anagram) - Use Hashset

#### **Array**

1. [Spiral Order](https://leetcode.com/problems/spiral-matrix) - Simple problem - The time spent is to figure out the boundaries, and edge cases(when right = left or up = down).
2. [Merge Intervals](https://leetcode.com/problems/merge-intervals) - Sort the intervals in nlogn and then just do a linear comparison.
3. [Insert Interval](https://leetcode.com/problems/insert-interval) - As the list is already sorted and has non overlapping intervals, its an easy problem which is similar to Merge Intervals
4. [Set Zeroes](https://leetcode.com/problems/set-matrix-zeroes) - Intuitive solution using additional set for row and column indices is easy. The no additional space solution is a bit tricky and read the code comments to understand that. 
5. [Longest Common Subsequence](https://leetcode.com/problems/longest-consecutive-sequence) - N iterator and do an inner loop only when you find the head of a sequence i.e curr - 1 not in nums_set. We use set for O(1) lookup and also to eliminate duplicates
5. [Product Except Self](https://leetcode.com/problems/product-of-array-except-self) - Build an array with left product and then calculate right product and the output array.
6. [Non-Overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals) - Similiar to merge intervals which needs sorting. In this while merging, just do a count instead.
7. [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements) - Use Quick-select to partition the array and move all k element to the right.

#### **Linked List**

1. [Detect Loop](https://leetcode.com/problems/linked-list-cycle) - Floyd's Cycle Detection Algorithm.
2. [Reorder List](https://leetcode.com/problems/reorder-list) - first and last ptrs on a list to traverse and merge them.
3. [Reverse LL](https://leetcode.com/problems/reverse-linked-list) - n iteration solution.

#### **Greedy**

1. [Can Jump](https://leetcode.com/problems/jump-game) - Simple bottom up solution using Greedy. Just use the lastPos pointer to solve the local optima. This problem can be solved using DP as well but the solution is worse ie O(n^2)

#### **Tree**

1. [Same Tree](https://leetcode.com/problems/same-tree) - Simple preorder traversal and equality check
2. [Max Depth](https://leetcode.com/problems/maximum-depth-of-binary-tree) - easy tree traversal and sum. This can be solved either using BFS iteration using stack or using recursion
3. [Validate BST](https://leetcode.com/problems/validate-binary-search-tree) - Medium question to find a simple trick. Each node in the tree should greater than max of its left and smaller than min of its right.
4. [Level Order Tree](https://leetcode.com/problems/binary-tree-level-order-traversal) - Easy Question which is solved using a Queue
5. [Contruct Binary Tree](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal) - Solved using inorder map(value, index),incrementing preorder index and a l and r for tracking size of subtree 
5. [Tree Max Sum Path](https://leetcode.com/problems/binary-tree-maximum-path-sum) - a hard question solved within half an hour :). Find the max at each node by comparing current node, max of left and max of right.
6. [Kth Smallest Element in BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst) - use inorder traversal iterative.
7. [Valid Tree](https://leetcode.com/problems/graph-valid-tree) - A Tree has only V-1 edges. So check this and if it passes, then check if all nodes are connected. No need to check if graph has cycles because connected graph with cycle should have more than n - 1 edges.
8. [Is Subtree](https://leetcode.com/problems/subtree-of-another-tree) - Easy impl using find and isSame methods but its O(N * M). Use Merkel Tree for O(N + M) solution. 

### **Graph**

1. [Clone Graph](https://leetcode.com/problems/clone-graph) - Can use BFS to traverse each node and get all the neighbours and a map to store the new nodes as keys.
2. [Number of Islands](https://leetcode.com/problems/number-of-islands) - a solution using DFS/BFS with set. It can also be solved using Union Find.
3. [Connected Components](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph) - Use BFS/DFS to traverse each connected component.
4. [Pacific Atlantic Water Flows](https://leetcode.com/problems/pacific-atlantic-water-flow) - use dfs to traverse all edges and individually compute visited for pacific and atlantic edges. The just perform an intersection at the end.
5. [Course Schedule](https://leetcode.com/problems/course-schedule) - Use DFS to find if there is a cycle.
### **Bit Manipulation**

1. [Reverse BIts for 32 bit unsigned number](https://leetcode.com/problems/reverse-bits) - use bitwise operators to mask and shift the input
2. [Count Set Bits](https://leetcode.com/problems/number-of-1-bits) - use mask and shift
3. [Bitwise Sum](https://leetcode.com/problems/sum-of-two-integers) - Read the solution section for proper understanding of the xor and and operations in the computation.
