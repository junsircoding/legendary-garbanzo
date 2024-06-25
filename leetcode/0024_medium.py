# -*- coding: utf-8 -*-

"""
Swap Nodes in pairs
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, var=0, next=None):
        self.var = var
        self.next = next

# Test ListNode
node8 = ListNode(var=8, next=None)
node7 = ListNode(var=7, next=node8)
node6 = ListNode(var=6, next=node7)
node5 = ListNode(var=5, next=node6)
node4 = ListNode(var=4, next=node5)
node3 = ListNode(var=3, next=node4)
node2 = ListNode(var=2, next=node3)
node1 = ListNode(var=1, next=node2)

head = node1

#while head:
#    print(head.var)
#    head = head.next
#
# Solution
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        dummy_head.next = head
        temp = dummy_head
        while temp.next and temp.next.next:
           node1 = temp.next
           node2 = temp.next.next
           temp.next = node2
           node1.next = node2.next
           node2.next = node1
           temp = node1
        return dummy_head.next

        # pre, pre.next = self, head
        # while pre.next and pre.next.next:
        #     a = pre.next
        #     b = a.next
        #     pre.next, b.next, a.next = b, a, b.next
        #     pre = a
        # return self.next

solution = Solution()
head = solution.swapPairs(head)


while head:
    print(head.var)
    head = head.next


