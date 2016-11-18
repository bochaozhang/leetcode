# A peak element is an element that is greater than its neighbors.

# Given an input array where num[i] =/= num[i+1], find a peak element and return its index.

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            if lo == hi:
                return lo
            mid = (lo + hi) / 2
            if nums[mid] < nums[mid+1]:
                lo = mid + 1
            else:
                hi = mid

if __name__ == "__main__":
    print Solution().findPeakElement([1,2,3,1])
