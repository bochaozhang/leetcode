# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = [x+1 for x in range(n)]
        return list(self.findComb(nums, k))        

    def findComb(self, nums, k):
        if k == 1:
            for num in nums:
                yield [num]
        else:
            for i in range(len(nums)):
                for item in self.findComb(nums[i+1:], k-1):
                    yield [nums[i]] + item

if __name__ == "__main__":
    print Solution().combine(4,2)
    print Solution().combine(4,3)
    print Solution().combine(5,2)
    print Solution().combine(6,5)
