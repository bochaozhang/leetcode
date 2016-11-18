# Given a 2D board and a word, find if the word exists in the grid.

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if board == []:
            return False
        visited = [[False] * len(board[0]) for i in range(len(board))]
        for i in range(len(visited)):
            for j in range(len(visited[0])):
                if self.findWord(board, word, visited, i, j, 0):
                    return True
        return False

    def findWord(self, board, word, visited, row, col, index):
        if index == len(word):
            return True
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or visited[row][col] or board[row][col] != word[index]:
            return False
        visited[row][col] = True
        if self.findWord(board, word, visited, row+1, col, index+1): return True 
        if self.findWord(board, word, visited, row-1, col, index+1): return True 
        if self.findWord(board, word, visited, row, col+1, index+1): return True 
        if self.findWord(board, word, visited, row, col-1, index+1): return True 
        visited[row][col] = False
        return False

if __name__ == "__main__":
    board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
    print Solution().exist(board,"ABCCED")
    print Solution().exist(board,"SEE")
    print Solution().exist(board,"ABCB")
