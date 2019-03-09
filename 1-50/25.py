class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def list_len(self, head):
        p1 = head
        cnt = 0
        while p1:
            cnt += 1
            p1 = p1.next
        return cnt

    def contact_list(self, l1, l2):
        p = l1
        while p.next:
            p = p.next
        p.next = l2

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None or k == 1:
            return head
        list_len = self.list_len(head)
        if list_len < k:
            return head
        final_head = None
        p1 = None
        flag = False
        while True:
            if p1 is None:
                if flag:
                    break
                else:
                    p1 = head
                    flag = True
            tmp_list = []
            i = 0
            while i < k and p1:
                tmp_list.append(p1)
                p1 = p1.next
                i += 1
            if len(tmp_list) < k:
                first = tmp_list[0]
            else:
                for j in range(k - 1, 0, -1):
                    tmp_list[j].next = tmp_list[j - 1]
                tmp_list[0].next = None
                first = tmp_list[-1]
            if final_head is None:
                final_head = first
            else:
                self.contact_list(final_head, first)
        if final_head is None:
            return head
        else:
            return final_head


def make_nodelist(nums):
    head = None
    p = None
    for num in nums:
        node = ListNode(num)
        if head is None:
            head = node
            p = node
        else:
            p.next = node
            p = p.next
    return head


if __name__ == '__main__':
    print(Solution().reverseKGroup(make_nodelist([1, 2, 3, 4, 5]), 2))
