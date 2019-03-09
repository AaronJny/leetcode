class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def mergeKLists(self, lists):
        ln = None
        pn = None
        ps = [node for node in lists if node]
        while len(ps) and all(ps):
            min_px = 0
            min_num = ps[0].val
            for i in range(1, len(ps)):
                if ps[i].val < min_num:
                    min_px = i
                    min_num = ps[i].val
            tmp_node = ListNode(min_num)
            if ln is None:
                ln = tmp_node
                pn = tmp_node
            else:
                pn.next = tmp_node
                pn = pn.next
            ps[min_px] = ps[min_px].next
            ps = [node for node in ps if node]
        return ln
