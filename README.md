[![Build Status](https://travis-ci.org/IamConstantine/LeetCodeFiddle.svg?branch=master)](https://travis-ci.org/IamConstantine/LeetCodeFiddle)
# LeetCodeFiddle
Solutions to LeetCode problems in Scala


## Hints:

#### **Divide and Conquer**

1. [Search in Rotated Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) - Use Binary search approach to solve in O(log n). Find the mid and check if right is sorted first ie compare l and mid. Binary search is called a _decrease and conquer_ problem instead of _divide and conquer_.


#### **Backtracking**

1. [Combination Sum](https://leetcode.com/problems/combination-sum) - Find all combinations for the given sum. Nothing to memoise here. You can use one node multiple times in the path to find the combination. But you cannot use your parent node once you have gone down the level.
