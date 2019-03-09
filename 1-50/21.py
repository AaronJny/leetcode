# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        l3 = None
        p3 = None
        while p1 and p2:
            if p1.val < p2.val:
                tmp_node = ListNode(p1.val)
                if l3 is None:
                    l3 = tmp_node
                    p3 = tmp_node
                else:
                    p3.next = tmp_node
                    p3 = p3.next
                p1 = p1.next
            else:
                tmp_node = ListNode(p2.val)
                if l3 is None:
                    l3 = tmp_node
                    p3 = tmp_node
                else:
                    p3.next = tmp_node
                    p3 = p3.next
                p2 = p2.next
        while p1:
            tmp_node = ListNode(p1.val)
            if l3 is None:
                l3 = tmp_node
                p3 = tmp_node
            else:
                p3.next = tmp_node
                p3 = p3.next
            p1 = p1.next
        while p2:
            tmp_node = ListNode(p2.val)
            if l3 is None:
                l3 = tmp_node
                p3 = tmp_node
            else:
                p3.next = tmp_node
                p3 = p3.next
            p2 = p2.next
        return l3
