# Given a sorted array of integers, find the starting and ending position of a given target value.

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # lower boundary
        lo = 0
        hi = len(nums) - 1
        while (lo < hi):
            mid = int((lo + hi) / 2)
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1
        if nums[lo] == target:
            lowerBoundary = lo
        else:
            return [-1,-1]
        # upper boundary
        lo = 0
        hi = len(nums) - 1
        while (lo < hi):
            mid = int((lo + hi) / 2) + 1
            if nums[mid] <= target:
                lo = mid
            else:
                hi = mid - 1
        if nums[hi] == target:
            upperBoundary = hi
        else:
            return [-1,-1]
        return [lowerBoundary,upperBoundary]

if __name__ == "__main__":
    print Solution().searchRange([5, 7, 7, 8, 8, 8, 10], 8)
    print Solution().searchRange([8, 8, 8, 8, 8, 8, 8], 8)
    print Solution().searchRange([8, 8, 8, 8, 8, 8, 8], 6)
