package com.constantine.fiddle.leetcode

import LongestSubString.lengthOfLongestSubstring
import org.scalatest.FunSuite

class LongestSubStringTest extends FunSuite {

  test("should find Length of longest non repeating character sequence"){
    assert(lengthOfLongestSubstring("abcabcbb") == 3)
    assert(lengthOfLongestSubstring("bbbbb") == 1)
    assert(lengthOfLongestSubstring("pwwkew") == 3)
    assert(lengthOfLongestSubstring("abba") == 2)
  }
}
