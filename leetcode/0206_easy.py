# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        list_node = [
            ListNode(val=1, next=2),
            ListNode(val=2, next=3),
            ListNode(val=3, next=4),
            ListNode(val=4, next=5),
            ListNode(val=5, next=None)
        ]

        new_list_node = [
            ListNode(val=1, next=None),
            ListNode(val=2, next=1),
            ListNode(val=3, next=2),
            ListNode(val=4, next=3),
            ListNode(val=5, next=4)
        ]
        """
        cur, prev = head, None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp            
        return prev

