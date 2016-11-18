# Suppose a sorted array is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                if nums[mid] > target and nums[left] <= target:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid  
        return -1

if __name__ == "__main__":
    print Solution().search([4,5,6,7,0,1,2], 4)
    print Solution().search([4,5,6,7,0,1,2], 2)
    print Solution().search([4,5,6,7,0,1,2], 8)
