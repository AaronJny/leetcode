class Solution:
    def largestRectangleArea(self, heights) -> int:
        n = len(heights)
        if n == 0:
            return 0
        lstack = []
        l = [0 for _ in range(n)]
        for i in range(n):
            if len(lstack) == 0:
                l[i] = 0
            else:
                while len(lstack):
                    if heights[lstack[-1]] >= heights[i]:
                        lstack.pop()
                    else:
                        break
                if len(lstack) == 0:
                    l[i] = 0
                else:
                    l[i] = lstack[-1] + 1
            lstack.append(i)
        rstack = []
        r = [0 for _ in range(n)]
        for i in range(n - 1, -1, -1):
            if len(rstack) == 0:
                r[i] = n - 1
            else:
                while len(rstack):
                    if heights[rstack[-1]] >= heights[i]:
                        rstack.pop()
                    else:
                        break
                if len(rstack) == 0:
                    r[i] = n - 1
                else:
                    r[i] = rstack[-1] - 1
            rstack.append(i)
        max_area = 0
        for i in range(n):
            max_area = max((r[i] - l[i] + 1) * heights[i], max_area)
        return max_area