# Follow up for "Unique Paths":

# Now consider if some obstacles are added to the grids. How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        steps = [[0 for x in range(101)] for x in range(101)]
        steps[0][1] = 1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if obstacleGrid[i-1][j-1] == 1:
                    steps[i][j] = 0
                else:
                    if i > 1 and obstacleGrid[i-2][j-1] == 1:
                        steps[i][j] = steps[i][j-1]
                    elif j > 1 and obstacleGrid[i-1][j-2] == 1:
                        steps[i][j] = steps[i-1][j]
                    else:
                        steps[i][j] = steps[i-1][j] + steps[i][j-1]
        return steps[m][n]

if __name__ == "__main__":
    print Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
    print Solution().uniquePathsWithObstacles([[0,0],[1,0]])
