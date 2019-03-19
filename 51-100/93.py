class Solution:
    def dfs(self, s, left, right, n, tmps: list, ipset: set):
        if left >= n:
            if len(tmps) == 4:
                ipset.add('.'.join(tmps))
        else:
            tmps.append(s[left:right])
            self.dfs(s, right, right + 1, n, tmps, ipset)
            tmps.pop()
            if s[left] != '0':
                x = 4 - (right - left)
                for i in range(1, x):
                    nr = right + i
                    if nr <= n and int(s[left:nr]) <= 255 and len(tmps) <= 4:
                        self.dfs(s, left, nr, n, tmps, ipset)

    def restoreIpAddresses(self, s: str):
        n = len(s)
        if n == 0:
            return []
        ipset = set()
        self.dfs(s, 0, 1, n, [], ipset)
        return list(ipset)