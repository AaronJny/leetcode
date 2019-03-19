class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            nums1[m:] = nums2
            return
        p1 = 0
        for num in nums2:
            while p1 < m and nums1[p1] <= num:
                p1 += 1
            for i in range(m, p1, -1):
                nums1[i] = nums1[i - 1]
            nums1[p1] = num
            m += 1
            p1 += 1