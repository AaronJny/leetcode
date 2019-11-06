class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        两两交换给定链表的节点
        :param head: 链表头结点
        :return:
        """
        # 如果链表为空，或链表长度为1，就不用交换了，直接返回
        if head is None or head.next is None:
            return head
        # p1作为一个游标，遍历整个链表，最开始指向头结点
        p1 = head
        # 现在last指定第三个节点
        last = p1.next.next
        # second指向第二个节点
        second = p1.next
        # 把第一个节点放到second后面去
        second.next = p1
        # 并且使 *前*第一个节点的next指向第三个节点last
        p1.next = last
        # 现在second是第一个节点，并且完成了第一个节点和第二个节点的交换
        head = second
        # 后面重复这个过程即可
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
        # 返回头节点
        return head