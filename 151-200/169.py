from collections import Counter


class Solution:
    def majorityElement(self, nums) -> int:
        counter = Counter(nums)
        return int(counter.most_common(1)[0][0])