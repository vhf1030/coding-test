# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val > list2.val:
            list1, list2 = list2, list1  # 작은애를 시작 노드로 설정
        result = p = list1
        while list2:
            if not p.next:
                p.next = list2
                return result
            if p.next.val > list2.val:
                tmp1 = p.next
                tmp2 = list2.next
                p.next = list2
                list2.next = tmp1
                list2 = tmp2
            p = p.next
        return result

        