# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        while head and head.val == val:
            head = head.next
        n_head = head
        while head and head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return n_head