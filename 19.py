# coding=utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def list_len(self, head):
        tmp_head = head
        cnt = 0
        while tmp_head:
            cnt += 1
            tmp_head = tmp_head.next
        return cnt

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = self.list_len(head)
        if length == 1:
            return None
        if length == n:
            return head.next
        tmp_head = head
        for i in range(length - n - 1):
            tmp_head = tmp_head.next
        remove_node = tmp_head.next
        next_node = remove_node.next
        tmp_head.next = next_node
        return head