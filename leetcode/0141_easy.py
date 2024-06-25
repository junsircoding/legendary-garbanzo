# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        1. 一直遍历到底，设定超时时间，超时就说明有环。不好掌控，万一链表特别长。
        2. 记录路径，当路径重复，说明有环。
        3. 设置快慢指针，当快慢指针相遇，说明有环。
        """
        # step = set()
        # cur = head
        # while cur:
        #     temp_step = (cur, cur.next)
        #     if temp_step in step:
        #         return True
        #     step.add(temp_step)
        #     cur = cur.next
        # return False

        fast = slow = head
        while slow and fast and fast.next:
            # 慢指针走一步
            slow = slow.next
            # 快指针走两步
            fast = fast.next.next
            # 快慢指针相遇，说明有环
            if slow is fast:
                return True
        return False

