# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) / 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                return mid
        return left

if __name__ == "__main__":
    print Solution().searchInsert([1,3,5,6], 5)
    print Solution().searchInsert([1,3,5,6], 2)
    print Solution().searchInsert([1,3,5,6], 7)
    print Solution().searchInsert([1,3,5,6], 0)
