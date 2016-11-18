# The n-queens puzzle is the problem of placing n queens on an n*n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n == 1:
            return [['Q']]
        elif n == 2 or n == 3:
            return []
        else:
            Solution.ans = []
            sol = []
            self.dfs(n, 0, sol)
            queenSol = []
            for list in Solution.ans:
                board = []
                for num in list:
                    row = ['.' for x in range(n)]
                    row[num] = 'Q'
                    board.append(''.join(row))
                queenSol.append(board)
            return queenSol    
        
    def dfs(self, n, rowNumber, sol):
        if rowNumber == n:
            Solution.ans.append(sol[:])
        else:
            for i in range(n):
                sol.append(i)
                if self.checkDiag(sol) and self.checkCol(sol):
                    self.dfs(n, rowNumber+1, sol)
                sol.pop()
            
    def checkDiag(self, rows):
        for i in range(len(rows)):
            for j in range(i+1, len(rows)):
                if abs(rows[i] - rows[j]) == j - i:
                    return False
        return True
    
    def checkCol(self, rows):
        cols = []
        for i in range(len(rows)):
            if rows[i] in cols:
                return False
            cols.append(rows[i])
        return True
        

if __name__ == "__main__":
    print Solution().solveNQueens(4)            
