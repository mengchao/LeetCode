#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (32.21%)
# Likes:    6402
# Dislikes: 1671
# Total Accepted:    1.1M
# Total Submissions: 3.4M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        inc = 0
        head = None
        tail = None
        
        while (l1 or l2):
            sum = 0
            if (l1):
                sum += l1.val
                l1 = l1.next

            if (l2):
                sum += l2.val
                l2 = l2.next

            sum += inc

            if sum > 9:
                sum -= 10
                inc = 1
            else:
                inc = 0

            currentElem = ListNode(sum)
            if tail is None:
                head = currentElem
            else:
                tail.next = currentElem

            tail = currentElem

        if inc != 0:
            currentElem = ListNode(1)
            if tail is None:
                head = currentElem
            else:
                tail.next = currentElem

        return head
        
# @lc code=end

