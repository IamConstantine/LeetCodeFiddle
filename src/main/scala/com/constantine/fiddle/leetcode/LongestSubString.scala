package com.constantine.fiddle.leetcode

import scala.collection.mutable

object LongestSubString {
  def lengthOfLongestSubstring(str: String): Int = {
    val visited = mutable.Map.empty[Char, Int]
    var i = 0
    var j = 0
    var max = 0
    while (j < str.length) {
      if (visited.contains(str(j))) {
        i = Math.max(i, visited(str(j)))
      }
      max = Math.max(max, j - i + 1)
      visited += (str(j) -> (j + 1))
      j += 1
    }
    max
  }
}