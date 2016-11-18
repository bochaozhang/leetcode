# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        return self.merge(intervals)

    def merge(self, intervals):
        # sort intervals according to start
        starts = []
        for interval in intervals:
            starts.append(interval.start)
        intervals = [x for (y, x) in sorted(zip(starts,intervals))]
        ans = []
        for interval in intervals:
            if ans == []:
                ans.append(interval)
            else:
                temp = ans[-1]
                if temp.end >= interval.start:
                    ans.pop()
                    ans.append(Interval(temp.start, max(temp.end, interval.end)))
                else:
                    ans.append(interval)
        return ans


if __name__ == "__main__":
    I = Solution().insert([Interval(1,2), Interval(3,5), Interval(6,7), Interval(8,10), Interval(12,16)], Interval(4,9))
    for item in I:
        print [item.start, item.end]

