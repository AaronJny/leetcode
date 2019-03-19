# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        new_head = None
        p2 = None
        p = head
        while p:
            tmpnode = ListNode(p.val)
            if new_head is None:
                new_head = tmpnode
                p2 = new_head
            else:
                p2.next = tmpnode
                p2 = p2.next
            if p.next and p.val == p.next.val:
                dup_num = p.val
                while p and p.val == dup_num:
                    p = p.next
            else:
                p = p.next

        return new_head