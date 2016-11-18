# Given an array of integers, every element appears twice except for one. Find that single one.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        store = 0
        for num in nums:
            store = store ^ num
        return store
           
if __name__ == "__main__":
    nums = [1,2,3,2,3]
    print Solution().singleNumber(nums) 
    nums = [1,0,3,0,3]
    print Solution().singleNumber(nums) 
