# coding=utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def list_len(self, head):
        """
        计算给定链表的长度
        :param head:
        :return:
        """
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
        # 获取链表的长度
        length = self.list_len(head)
        # 长度为1，移除完就没了，返回None
        if length == 1:
            return None
        # 长度为n的话，相当于移除了头结点，直接返回head.next即可
        if length == n:
            return head.next
        # 否则的话，先找到倒数第n个节点的前一个节点
        tmp_head = head
        for i in range(length - n - 1):
            tmp_head = tmp_head.next
        # 然后通过改变next指向，移除掉倒数第n个节点即可。
        remove_node = tmp_head.next
        next_node = remove_node.next
        tmp_head.next = next_node
        return head