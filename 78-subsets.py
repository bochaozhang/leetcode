# Given a set of distinct integers, nums, return all possible subsets.

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = [[]]
        for k in range(len(nums)+1):
            ans += self.findComb(nums, k)
        return ans

    def findComb(self, nums, k):
        if k == 1:
            for num in nums:
                yield [num]
        else:
            for i in range(len(nums)):
                for item in self.findComb(nums[i+1:], k-1):
                    yield [nums[i]] + item

if __name__ == "__main__":
    print Solution().subsets([1,2,3])
