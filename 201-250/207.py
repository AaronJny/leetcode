class Solution:

    def find_zero_in_point(self, in_degrees, v_set):
        """
        检查是否还存在入度为0的点

        Args:
            in_degrees:记录入度的列表
            v_set:剩余顶点的集合

        Returns:

        """
        for x in v_set:
            if in_degrees[x] == 0:
                return True, x
        return False, 0

    def canFinish(self, numCourses, prerequisites) -> bool:
        graph = {x: [] for x in range(numCourses)}
        in_degrees = {x: 0 for x in range(numCourses)}
        v_set = set()
        for end, begin in prerequisites:
            graph[begin].append(end)
            in_degrees[end] += 1
            v_set.add(end)
            v_set.add(begin)
        while True:
            ok, v = self.find_zero_in_point(in_degrees, v_set)
            # 找到入度为0的点
            if ok:
                # 先移除
                v_set.remove(v)
                # 然后减少相应边的入度
                for x in graph[v]:
                    in_degrees[x] -= 1
            # 找不到入度为0的点了
            else:
                # 如果还有点存在，那就说明存在了环，无法解决依赖问题
                if v_set:
                    return False
                # 所有点都被移除了，能够依赖
                else:
                    return True