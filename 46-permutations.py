# Given a collection of distinct numbers, return all possible permutations.

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        return list(self.heap(n, nums)) 
        
    def heap(self, n, A):
        if n == 1:
            yield A[:]
        else:
            for i in range(n-1):
                for item in self.heap(n-1, A): 
                    yield item
                if n % 2 == 0:
                    A[i], A[n-1] = A[n-1], A[i]
                elif n % 2 == 1:
                    A[0], A[n-1] = A[n-1], A[0]
            for item in  self.heap(n-1, A): 
                yield item
        
if __name__ == "__main__":
    print Solution().permute([1,2,3])
