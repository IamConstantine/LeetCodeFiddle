[![Build Status](https://travis-ci.org/IamConstantine/LeetCodeFiddle.svg?branch=master)](https://travis-ci.org/IamConstantine/LeetCodeFiddle)
# LeetCodeFiddle
Solutions to LeetCode problems in Scala


## Hints:

#### **Dynamic Programming**

1. [Unique Paths](https://leetcode.com/problems/unique-paths) - Use the dp array to solve this in O(mn) complexity. Instantiate first row and first column with 1 as its a known valid path to m.n. There's an intuitive recursive + memoisation solution as well.
2. [String Two Digit Decoding](https://leetcode.com/problems/decode-ways) - The DP array solution. Each non zero is a 1 ie dp[i] = dp[i-1] and each two digits >=10 is dp[i] += dp[i-2].
3. [Word Break](https://leetcode.com/problems/word-break) - DP Recursion + memoisation
4. [House Robber](https://leetcode.com/problems/house-robber) - Calculate max(i + i-2, i-1). 
5. [Long Increasing Sequence](https://leetcode.com/problems/longest-increasing-subsequence) - An N^2 algo to compute the seq length for every ith value.
6. [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence) - use bottom up on a dp[text1+1][text2+1] array. Refer the solution section for more details.
7. [House Robber II](https://leetcode.com/problems/house-robber-ii) - compute max of house_robber(1, N) and house_robber(0, N-1).
8. [Stone Game IV](https://leetcode.com/problems/stone-game-iv) - use dfs with memo or dp to calculate for each value of n from 1 to n + 1.
9. [Count Delivery Orders](https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options) - Use top-down DP with memo to solve the problem using permutations.

#### **Divide and Conquer**

1. [Search in Rotated Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) - Use Binary search approach to solve in O(log n). Find the mid and check if right is sorted first ie compare l and mid. Binary search is called a _decrease and conquer_ problem instead of _divide and conquer_.
2. [Find Min in Rotated Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array) - Use Binary Search to find min in search space.
3. [Sort Linked List](https://leetcode.com/problems/sort-list) - Use merge sort.

#### **Backtracking**

1. [Combination Sum](https://leetcode.com/problems/combination-sum) - Find all combinations for the given sum. Nothing to memoise here. You can use one node multiple times in the path to find the combination. But you cannot use your parent node once you have gone down the level.
2. [Word Search](https://leetcode.com/problems/word-search) - Intuitive solution using visited matrix and traverse all 3 directions from one cell approach.
3. [Word Search II](https://leetcode.com/problems/word-search-ii) - Use Trie of all the words and then traverse the board like Word Search Problem. We would need to pop leaves when match is met to avoid exploration of visited trie nodes.

#### **Strings**

1.  [Group Anagrams](https://leetcode.com/problems/group-anagrams) - can define group key using sorted strings(O(NKlogK)) or character count(0(NK)) approach
2.  [String Minimum Window](https://leetcode.com/problems/minimum-window-substring) - use length of t and l and r ptrs for window to solve this in O(2S)
3.  [Validate Palindrome](https://leetcode.com/problems/valid-palindrome) - Easy problem solved using a l and r pointer.
4.  [Is Anagram ?](https://leetcode.com/problems/valid-anagram) - Use Hashset
5.  [String Codec](https://leetcode.com/problems/encode-and-decode-strings) - use 4 byte chunked encoding for storing length of each string in list. 
6.  [Group Shifted Strings](https://leetcode.com/problems/group-shifted-strings) - create a group key based on the shifts.
7.  [Find Anagrams](https://leetcode.com/problems/find-all-anagrams-in-a-string) - use two counters - one for p and another to track what has been seen till now and update accordingly.
8.  [Check Inclusion](https://leetcode.com/problems/permutation-in-string) - Use Sliding window with counter.
9.  [K length Substring No Repeats](https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters) - use sliding window.
10. [Strobogrammatic Number - II](https://leetcode.com/problems/strobogrammatic-number-ii) - use level order to find the required combinations.
11. [Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement) - use a sliding window to figure out the valid char set.
12. [Count Pallindromic Substrings](https://leetcode.com/problems/palindromic-substrings) - use an expand around center approach.
13. [Score of Parantheses](https://leetcode.com/problems/score-of-parentheses) - count cores ie ().

#### **Array**

1.  [Spiral Order](https://leetcode.com/problems/spiral-matrix) - Simple problem - The time spent is to figure out the boundaries, and edge cases(when right = left or up = down).
2.  [Merge Intervals](https://leetcode.com/problems/merge-intervals) - Sort the intervals in nlogn and then just do a linear comparison.
3.  [Insert Interval](https://leetcode.com/problems/insert-interval) - As the list is already sorted and has non overlapping intervals, its an easy problem which is similar to Merge Intervals
4.  [Set Zeroes](https://leetcode.com/problems/set-matrix-zeroes) - Intuitive solution using additional set for row and column indices is easy. The no additional space solution is a bit tricky and read the code comments to understand that. 
5.  [Longest Common Subsequence](https://leetcode.com/problems/longest-consecutive-sequence) - N iterator and do an inner loop only when you find the head of a sequence i.e curr - 1 not in nums_set. We use set for O(1) lookup and also to eliminate duplicates
5.  [Product Except Self](https://leetcode.com/problems/product-of-array-except-self) - Build an array with left product and then calculate right product and the output array.
6.  [Non-Overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals) - Similiar to merge intervals which needs sorting. In this while merging, just do a count instead.
7.  [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements) - Use Quick-select to partition the array and move all k element to the right.
8.  [Max Distance to Closest](https://leetcode.com/problems/maximize-distance-to-closest-person) - Use a simple n algorithm to find mid between two allocated seats.
9.  [Meeting Rooms](https://leetcode.com/problems/meeting-rooms) - sort and then compare i end with i +1 start.
10. [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii) - sort by start time and use heap on end time to get the no of rooms required or separate start and end ts and work on that using two pointers.
11. [Can Place Flowers](https://leetcode.com/problems/can-place-flowers) - start from imaginary prev -2 and find no of plots which can be used between two flowers.
12. [Monotonic Array](https://leetcode.com/problems/monotonic-array) - set inc and dec to True and then start the loop to unset the required flags based on the order of growth.
13. [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas) - use binary search to find the required rate in 1, max(piles) search space.
14. [Gas Station](https://leetcode.com/problems/gas-station) - take two counters. Total has all deficit : gas - cost and curr tracks consumption from a good starting point.
15. [Sequential Numbers](https://leetcode.com/problems/sequential-digits) - Use a sliding window on '123456789' string.
16. [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram) - use stack to push elements in increasing order and then pop and calculate the area for each popped element.
17. [Rotate Array](https://leetcode.com/problems/rotate-array) - Reverse whole list and then 0,k-1 and k, end.
18. [4 Sum ii](https://leetcode.com/problems/4sum-ii) - run a loop on k//2 lists to generate counter and then run on the remaining to find the complement.
19. [Find Max Length of Zeros and Ones in array](https://leetcode.com/problems/contiguous-array) - a very high IQ implementation using map to track the count of 0s and 1s and track max length.
20. [Subarray Sum](https://leetcode.com/problems/subarray-sum-equals-k) - use map to store cumulative and the no of occurences.
21. [Subsets](https://leetcode.com/problems/subsets) - Use cascading to solve in N * 2 ^ N.
22. [Remove K Digits](https://leetcode.com/problems/remove-k-digits) - Use a stack to compare left and curr digit.
23. [Champagne Tower](https://leetcode.com/problems/champagne-tower) - Use 2D array to track progress of glasses.
34. [Campus Bikes](https://leetcode.com/problems/campus-bikes] - Use bucketing to sort out all distance pairs and then pick first N workers pairs.
35. [Max Frequency Stack](https://leetcode.com/problems/maximum-frequency-stack) - Two approaches: One can be done using Max Heap with a triplet of (freq, index, val) and another one can done using freq group and a max variable. 

#### **Linked List**

1. [Detect Loop](https://leetcode.com/problems/linked-list-cycle) - Floyd's Cycle Detection Algorithm.
2. [Reorder List](https://leetcode.com/problems/reorder-list) - first and last ptrs on a list to traverse and merge them.
3. [Reverse LL](https://leetcode.com/problems/reverse-linked-list) - n iteration solution.

#### **Greedy**

1. [Can Jump](https://leetcode.com/problems/jump-game) - Simple bottom up solution using Greedy. Just use the lastPos pointer to solve the local optima. This problem can be solved using DP as well but the solution is worse ie O(n^2)
2. [Remove Covered Interval](https://leetcode.com/problems/remove-covered-intervals) - sort start asc and end desc and then use only end time to figure out actual count.
3. [Validate Stack Sequences](https://leetcode.com/problems/validate-stack-sequences) - use a greedy approach to start popping once u find a match.
4. [Remove Duplicate Characters](https://leetcode.com/problems/remove-duplicate-letters) - use greedy with stack approach.
5. [Min Domino Rotations](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row) - Use greedy approach on an any arbitrary index.

#### **Tree**

1.  [Same Tree](https://leetcode.com/problems/same-tree) - Simple preorder traversal and equality check
2.  [Max Depth](https://leetcode.com/problems/maximum-depth-of-binary-tree) - easy tree traversal and sum. This can be solved either using BFS iteration using stack or using recursion
3.  [Validate BST](https://leetcode.com/problems/validate-binary-search-tree) - Medium question to find a simple trick. Each node in the tree should greater than max of its left and smaller than min of its right.
4.  [Level Order Tree](https://leetcode.com/problems/binary-tree-level-order-traversal) - Easy Question which is solved using a Queue
5.  [Contruct Binary Tree](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal) - Solved using inorder map(value, index),incrementing preorder index and a l and r for tracking size of subtree 
5.  [Tree Max Sum Path](https://leetcode.com/problems/binary-tree-maximum-path-sum) - a hard question solved within half an hour :). Find the max at each node by comparing current node, max of left and max of right.
6.  [Kth Smallest Element in BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst) - use inorder traversal iterative.
7.  [Valid Tree](https://leetcode.com/problems/graph-valid-tree) - A Tree has only V-1 edges. So check this and if it passes, then check if all nodes are connected. No need to check if graph has cycles because connected graph with cycle should have more than n - 1 edges.
8.  [Is Subtree](https://leetcode.com/problems/subtree-of-another-tree) - Easy impl using find and isSame methods but its O(N * M). Use Merkel Tree for O(N + M) solution. 
9.  [Least Common Ancestor BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree) - Return the parent which caused for p and q.
10. [Least Common Ancestor Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree) - count number of matches from current + left + right>=2. If it matches this condition, the curr node is lca.
11. [Find Median in Data Stream](https://leetcode.com/problems/find-median-from-data-stream) - It can be solved using Heap or AVL. Two Heap solution is relatively easy. Use a maxheap for lower half and minheap for upper half and then the median elements can be accessed at the root.
12. [Word Dictionary](https://leetcode.com/problems/design-add-and-search-words-data-structure) - Use Trie to solve for defined words and for searches with dots use recursion.
13. [Nearest Right Node](https://leetcode.com/problems/find-nearest-right-node-in-binary-tree) - Use BFS to track levels and then return first node after search node in the Q.
13. [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix) - use Trie to solve this.
14. [Max Xor Number](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array) - Use Bit Trie to find best xor pair for a number.
15. [Width Of Tree](https://leetcode.com/problems/maximum-width-of-binary-tree) - Use BFS or DFS.

### **Graph**

1.  [Clone Graph](https://leetcode.com/problems/clone-graph) - Can use BFS to traverse each node and get all the neighbours and a map to store the new nodes as keys.
2.  [Number of Islands](https://leetcode.com/problems/number-of-islands) - a solution using DFS/BFS with set. It can also be solved using Union Find.
3.  [Connected Components](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph) - Use BFS/DFS to traverse each connected component.
4.  [Pacific Atlantic Water Flows](https://leetcode.com/problems/pacific-atlantic-water-flow) - use dfs to traverse all edges and individually compute visited for pacific and atlantic edges. The just perform an intersection at the end.
5.  [Course Schedule](https://leetcode.com/problems/course-schedule) - Use DFS to find if there is a cycle.
6.  [Earliest Acquaintance](https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends) - Sort on logtime and then use Union Find to reduce groups.
7.  [Count Ships in Sea](https://leetcode.com/problems/number-of-ships-in-a-rectangle) - Use divide and conquer to break the search space into 4 quads.
8.  [Word Ladder](https://leetcode.com/problems/word-ladder) - use BFS to traverse all levels.
9.  [Alien Dictionary](https://leetcode.com/problems/alien-dictionary) - use topological sort.
10. [Shortest Path to traverse all nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes) - use dfs with visited bitmap.

### **Bit Manipulation**

1. [Reverse BIts for 32 bit unsigned number](https://leetcode.com/problems/reverse-bits) - use bitwise operators to mask and shift the input
2. [Count Set Bits](https://leetcode.com/problems/number-of-1-bits) - use mask and shift
3. [Bitwise Sum](https://leetcode.com/problems/sum-of-two-integers) - Read the solution section for proper understanding of the xor and and operations in the computation.
