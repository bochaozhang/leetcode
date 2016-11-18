# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxValue = max(nums)
        tempMax = nums[0]
        for i in range(1,len(nums)):
            tempMax = max(nums[i], tempMax+nums[i])
            maxValue = max(maxValue, tempMax)
        return maxValue

if __name__ == "__main__":
    print Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
