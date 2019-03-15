# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:

    def union(self, interval_a, interval_b):
        return Interval(interval_a.start, max(interval_a.end, interval_b.end))

    def is_intersected(self, interval_a, interval_b):
        if interval_a.start <= interval_b.start <= interval_a.end:
            return True
        else:
            return False

    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda x: (x.start, -x.end))
        result = []
        tmp_interval = None
        for interval in intervals:
            if tmp_interval is None:
                tmp_interval = Interval(interval.start, interval.end)
                continue
            if self.is_intersected(tmp_interval, interval):
                tmp_interval = self.union(tmp_interval, interval)
            else:
                result.append(Interval(tmp_interval.start, tmp_interval.end))
                tmp_interval = Interval(interval.start, interval.end)
        if tmp_interval:
            result.append(tmp_interval)
        return result
