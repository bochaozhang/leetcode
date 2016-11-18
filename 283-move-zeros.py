# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

class Solution(object):
    def moveZeros(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        non_zeros = 0
        for item in nums:
            if item != 0:
                non_zeros += 1
        while i <= non_zeros-1:
            while nums[i] == 0:
                for j in range(i,len(nums)-1):
                    nums[j] = nums[j+1]
                nums[len(nums)-1] = 0
            else:
                i += 1

        return nums

    def moveZeros_Pivot(self, nums):
        """
        Pivot
        """
        left_most = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[left_most] = nums[left_most], nums[i]
                left_most += 1

        return nums            

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    nums = Solution().moveZeros_Pivot(nums)
    for item in nums:
        print item
                
