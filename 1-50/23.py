class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def mergeKLists(self, lists):
        # 结果链表头结点
        ln = None
        # 指向结果链表的指针
        pn = None
        # 指向给定链表列表的指针列表，其中空链表将不会加入列表中
        ps = [node for node in lists if node]
        # 当指针列表不为空时
        while len(ps) and all(ps):
            # 指针列表中，指向节点的值最小的指针在列表中的下标，默认为0
            min_px = 0
            # 指针指向节点的最小值，默认为第一个指针指向结果的值
            min_num = ps[0].val
            # 检查所有指针指向节点，找出节点值最小的指针
            for i in range(1, len(ps)):
                # 当碰到值更小的节点时，更新最小节点指针在列表中的下标和最小值
                if ps[i].val < min_num:
                    min_px = i
                    min_num = ps[i].val
            # 这时，我们已经获取到了本次最小的值，创建一个新节点
            tmp_node = ListNode(min_num)
            # 将它加入到结果链表中
            # 当结果链表头结点为空时
            if ln is None:
                # 使用这个节点作为头结点
                ln = tmp_node
                # 结果链表的指针指向这个节点
                pn = tmp_node
            # 当不为空时
            else:
                # 结果链表的指针的next指向这个节点
                pn.next = tmp_node
                # 结果链表指针后移一位
                pn = pn.next
            # 值最小的节点对应的指针后移一位
            ps[min_px] = ps[min_px].next
            # 剔除掉走到头的指针，重复上述操作
            ps = [node for node in ps if node]
        # 返回结果链表
        return ln
