# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have
# exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
import copy
from typing import Optional

from Cython.Compiler.ExprNodes import ListNode


def twoSum(nums: list, target: int) -> list:
    for num in nums:
        first_index, second_index = None, None
        if target - num in nums[nums.index(num) + 1::]:
            first_index = nums.index(num)
            nums.remove(num)
            second_index = nums.index(
                target - num
            )
            return [first_index, second_index + 1]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

solution = Solution()
result = solution.addTwoNumbers(l1, l2)

while result:
    print(result.val, end=" -> " if result.next else "\n")
    result = result.next
