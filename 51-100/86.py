# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None
        t1 = None
        t2 = None
        p = head
        p1 = t1
        p2 = t2
        while p:
            val = p.val
            tmpnode = ListNode(val)
            if val < x:
                if t1 is None:
                    t1 = tmpnode
                    p1 = t1
                else:
                    p1.next = tmpnode
                    p1 = p1.next
            else:
                if t2 is None:
                    t2 = tmpnode
                    p2 = t2
                else:
                    p2.next = tmpnode
                    p2 = p2.next
            p = p.next
        if t1:
            p1.next = t2
            return t1
        else:
            return t2