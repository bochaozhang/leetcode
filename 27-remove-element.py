# Given an array and a value, remove all instances of that value in place and return the new length.

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[n] = nums[i]
                n += 1
        return n

if __name__ == "__main__":
    print Solution().removeElement([1,2,1,3,5],1)
