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
    def isSubsequenceV2(self, s, t):
        i=0
        if len(s)==0:
            return True
        for Char in t:
            if s[i] == Char:
                i +=1
            if i == len(s):
                return True
        return False
