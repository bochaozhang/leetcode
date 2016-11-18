# Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        rest = [1] * n
        left = right = 1
        for i in range(1,n):
            left *= nums[i-1]
            rest[i] *= left
        for i in range(n-2,-1,-1):
            right *= nums[i+1]
            rest[i] *= right
        return rest

if __name__ == "__main__":
    print Solution().productExceptSelf([1,2,3,4])
