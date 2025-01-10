# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = p = ListNode()
        q = 0
        while l1 or l2:
            value = l1.val + l2.val + q
            q, r = divmod(value, 10)
            p.val = r
            l1 = l1.next
            l2 = l2.next
            if l1 or l2 or q:
                p.next = ListNode()
                p = p.next
            if not l1 and not l2:
                if q:
                    p.val = q
                return result
            if not l1:
                l1 = ListNode()
            if not l2:
                l2 = ListNode()

        return result
