# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

# Each number in C may only be used once in the combination.

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        Solution.ans = []
        sol = []
        self.dfs(target, candidates, 0, sol)
        return [list(x) for x in set(tuple(x) for x in Solution.ans)]

    def dfs(self, target, candidates, start, sol):
        if target < 0:
            return
        elif target == 0:
            Solution.ans.append(sol[:])
        else:
            i = start
            while i < len(candidates) and candidates[i] <= target:
                sol.append(candidates[i])
                self.dfs(target - candidates[i], candidates, i+1, sol)
                sol.pop()
                i += 1

if __name__ == "__main__":
    print Solution().combinationSum2([10,1,2,7,6,1,5], 8)
