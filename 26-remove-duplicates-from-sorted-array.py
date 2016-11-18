# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        n = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[n] = nums[i]
                n += 1
        return n

if __name__ == "__main__":
    print Solution().removeDuplicates([])
    print Solution().removeDuplicates([1])
    print Solution().removeDuplicates([1,1,2])
    print Solution().removeDuplicates([1,2,3,3,4,5,5,6])
