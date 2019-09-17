class Solution:
    def find_num(self, target, left, right, numbers):
        while left < right:
            mid = (left + right) >> 1
            if numbers[mid] > target:
                right = mid - 1
            elif numbers[mid] < target:
                left = mid + 1
            else:
                return mid
        if numbers[left] == target:
            return left
        return -1

    def twoSum(self, numbers, target: int):
        n = len(numbers)
        for i in range(n):
            num = numbers[i]
            pos = self.find_num(target - num, i + 1, n - 1, numbers)
            if pos == -1:
                continue
            return [i + 1, pos + 1]