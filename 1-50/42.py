class Solution:

    def find_left_pos(self, height, pos):
        left_ok = False
        n = len(height)
        left_pos = pos - 1
        while left_pos >= 0:
            if height[left_pos] > height[pos]:
                left_ok = True
                break
            elif height[left_pos] < height[pos]:
                break
            left_pos -= 1
        return left_ok, left_pos

    def find_right_pos(self, height, pos):
        right_ok = False
        n = len(height)
        right_pos = pos + 1
        while right_pos < n:
            if height[right_pos] > height[pos]:
                right_ok = True
                break
            elif height[right_pos] < height[pos]:
                break
            right_pos += 1
        return right_ok, right_pos

    def find_lower_pos(self, height):
        n = len(height)
        lefts = []
        for i in range(1, n):
            if height[i] < height[i - 1]:
                lefts.append(i)
        ac = []
        for pos in lefts:
            for i in range(pos + 1, n):
                if height[pos] < height[i]:
                    ac.append(pos)
                    break
                elif height[pos] > height[i]:
                    break
                i += 1
        return ac

    def trap(self, height: list) -> int:
        n = len(height)
        if n == 0:
            return 0
        INF = 1 << 30
        result = 0
        min_height = 0
        while True:
            cur_min_height = min(filter(lambda x: x >= min_height, height))
            max_height = max(height)
            if cur_min_height >= max_height:
                break
            # 找出当前可用的最低点
            min_pos = self.find_lower_pos(height)
            min_filled_height = INF
            for pos in min_pos:
                # 检查最低点是否可用
                left_ok, left_pos = self.find_left_pos(height, pos)
                right_ok, right_pos = self.find_right_pos(height, pos)
                if left_ok and right_ok:
                    m = min(height[left_pos], height[right_pos])
                    min_filled_height = min(min_filled_height, m)
                    for x in range(left_pos + 1, right_pos):
                        result += m - height[x]
                        height[x] = m
            if min_filled_height == INF:
                break
            min_height = min_filled_height
        return result