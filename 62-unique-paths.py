# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        steps = [[0 for x in range(101)] for x in range(101)]
        steps[0][1] = 1
        for i in range(1,m+1):
            for j in range(1,n+1):
                steps[i][j] = steps[i - 1][j] + steps[i][j-1]
        return steps[m][n]

if __name__ == "__main__":
    print Solution().uniquePaths(5,5)
