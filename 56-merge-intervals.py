# Given a collection of intervals, merge all overlapping intervals.

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
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
    I = Solution().merge([Interval(1,3), Interval(2,6), Interval(4,5), Interval(8,10), Interval(15,18)])
    for item in I:
        print [item.start, item.end]
