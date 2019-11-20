#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (44.76%)
# Likes:    12503
# Dislikes: 434
# Total Accepted:    2.3M
# Total Submissions: 5.2M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# Example:
# 
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
# 
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numPosDict = {}
        for i, currentNum in enumerate(nums):

            # find prevous num element which sums up to target
            numToFind = target - currentNum
            j = numPosDict.get(numToFind)
            if j != None:
                return [j, i]
            
            # no previous num element could sums up to target, store current num and pos
            numPosDict[currentNum] = i
        
# @lc code=end

