# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        # record first row and column
        for j in range(n):
            if matrix[0][j] == 0:
                firstRow = True
                break
            else:
                firstRow = False
        for i in range(m):
            if matrix[i][0] == 0:
                firstColumn = True
                break
            else:
                firstColumn = False
        # record rest using first row and column
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        # set rest to zeroes
        for j in range(1,n):
            if matrix[0][j] == 0:
                for i in range(1,m):
                    matrix[i][j] = 0
        for i in range(1,m):
            if matrix[i][0] == 0:
                matrix[i] = [0] * n
        # set first row and column to zeroes
        if firstRow:
            matrix[0] = [0] * n
        if firstColumn:
            for i in range(m):
                matrix[i][0] = 0
        return matrix

if __name__ == "__main__":
    print Solution().setZeroes([[0,1],[1,1],[1,1]])
