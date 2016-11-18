# Follow up for N-Queens problem.

# Now, instead outputting board configurations, return the total number of distinct solutions.

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n == 1:
            return [['Q']]
        elif n == 2 or n == 3:
            return []
        else:
            Solution.ans = 0
            sol = []
            self.dfs(n, 0, sol)
            return Solution.ans    
        
    def dfs(self, n, rowNumber, sol):
        if rowNumber == n:
            Solution.ans += 1
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
    print Solution().totalNQueens(5)            
