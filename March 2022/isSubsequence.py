"""
LeetCode challenge #392: is Subsequence
https://leetcode.com/problems/is-subsequence/
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by
deleting some (can be none) of the characters without disturbing the relative
positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""
class Solution(object):
    """
    this solution can be improved upon as the letters in s must appear sequentially in t
    """
    def isSubsequence(self, s, t):
        length=0
        previous=-1
        if len(s)==0:
            return True
        for i, iValue in enumerate(s):
            for j, jValue in enumerate(t):
                if iValue == jValue and j > previous:
                    length += 1
                    previous = j
                    if length == len(s):
                        return True
                    break
        return False
