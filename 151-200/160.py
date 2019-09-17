# -*- coding: utf-8 -*-
# @File  : do3.py
# @Author: AaronJny
# @Date  : 2019/06/13
# @Desc  :


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def list_len(self, head):
        p = head
        cnt = 0
        while p:
            cnt += 1
            p = p.next
        return cnt

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        m = self.list_len(headA)
        n = self.list_len(headB)
        p1 = headA
        p2 = headB
        if m > n:
            x = m - n
            while x:
                p1 = p1.next
                x -= 1
        else:
            x = n - m
            while x:
                p2 = p2.next
                x -= 1
        x = min(m, n)
        while x:
            if p1 is p2:
                return p1
            x -= 1
            p1 = p1.next
            p2 = p2.next
        return None
