ss# Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

# The same repeated number may be chosen from C unlimited number of times.

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        Solution.ans = []
        self.dfs(target, candidates, 0, [])
        return Solution.ans

    def dfs(self, target, candidates, start, sol):
        if target < 0:
            return
        elif target == 0:
            Solution.ans.append(sol[:])
        else:
            i = start
            while i < len(candidates) and candidates[i] <= target:
                sol.append(candidates[i])
                self.dfs(target-candidates[i], candidates, i, sol)
                sol.pop()    
                i += 1

if __name__ == "__main__":
    print Solution().combinationSum([2,3,6,7], 7)
