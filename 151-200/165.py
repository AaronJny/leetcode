class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # 使用.分割，将每个部分的版本表示都转成数字，构成一个int列表
        v1 = [int(x) for x in version1.split('.')]
        v2 = [int(x) for x in version2.split('.')]
        # 尾部的为0的版本号都是无效的，直接移除
        while v1 and v1[-1] == 0:
            v1.pop()
        while v2 and v2[-1] == 0:
            v2.pop()
        # 然后直接比较即可
        if v1 > v2:
            return 1
        if v2 > v1:
            return -1
        return 0