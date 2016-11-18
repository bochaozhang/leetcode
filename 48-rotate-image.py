# You are given an n x n 2D matrix representing an image.

# Rotate the image by 90 degrees (clockwise).

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            for j in range(n/2):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
        return matrix

if __name__ == "__main__":
    m = Solution().rotate([[11,12,13,14],[21,22,23,24],[31,32,33,34],[41,42,43,44]])
    for item in m:
        print item
