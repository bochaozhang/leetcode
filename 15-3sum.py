# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        s = []
        counted = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] not in counted:
                twos = self.twoSum(nums[i+1:],-nums[i])
                if twos != []:
                    for sums in twos:
                        s.append([nums[i],sums[0],sums[1]])
            counted.append(nums[i])    
        return s           
        
    def twoSum(self, nums, target):
        counted = []
        s = []
        for i in range(len(nums)):
            if nums[i] not in counted:
                if target - nums[i] in nums[i+1:]:
                    s.append([nums[i], target - nums[i]])
            counted.append(nums[i])
        return s    

if __name__ == "__main__":
    print Solution().threeSum([0,0])
    print Solution().threeSum([0,0,0])
    print Solution().threeSum([0,0,0,0])
    print Solution().threeSum([-1,0,1])
