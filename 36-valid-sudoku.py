# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # board size
        if len(board) != 9:
            return False
        n = map(len,board)
        for number in n:
            if number != 9:
                return False
        # 0 < number < 10
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.' and (board[i][j] < '1' or board[i][j] > '9'):
                    return False
        # unique number row
        for i in range(9):
            string = board[i].replace('.','')
            if len(string) != len(set(string)):
                return False
        # unique number column
        for i in range(9):
            string = ''
            for j in range(9):
                if board[j][i] != '.':
                    string += board[j][i]
            if len(string) != len(set(string)):
                return False       
        # unique number in sub-box
        for i in range(0,8,3):
            for j in range(0,8,3):
                string = ''
                for p in range(3):
                    for q in range(3):
                        if board[i+p][j+q] != '.':
                            string += board[i+p][j+q]
                if len(string) != len(set(string)):
                    return False
        return True
        
if __name__ == "__main__":
    print Solution().isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])
    print Solution().isValidSudoku([".8765&3210","2........","3........","4........","5........","6........","7........","8........","9........"])
    print Solution().isValidSudoku([".87654$21","2........","3........","4........","5........","6........","7........","8........","9........"])
    print Solution().isValidSudoku([".87654322","2........","3........","4........","5........","6........","7........","8........","9........"])
    print Solution().isValidSudoku([".87654321","28.......","3........","4........","5........","6........","7........","8........","9........"])
    print Solution().isValidSudoku([".87654321","2.8......","3........","4........","5........","6........","7........","8........","9........"])
