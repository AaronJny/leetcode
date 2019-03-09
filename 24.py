class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        p1 = head
        last = p1.next.next
        second = p1.next
        second.next = p1
        p1.next = last
        head = second
        while p1.next:
            if p1.next.next is None:
                break
            first = p1.next
            second = first.next
            last = second.next
            p1.next = second
            second.next = first
            first.next = last
            p1 = first
        return head