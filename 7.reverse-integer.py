#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.54%)
# Likes:    2609
# Dislikes: 4084
# Total Accepted:    869.7K
# Total Submissions: 3.4M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
# 
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        sign = 1
        base = 1

        if (x < 0):
            sign = -1
            x *= -1

        while (x >= base * 10):
            base *= 10

        while (x > 0):
            result += (x % 10) * base
            x //= 10
            base /= 10

        result *= sign

        if (result > pow (2, 31) - 1 or result < -1 * pow (2, 31)):
            result = 0

        return int(result)

# @lc code=end

