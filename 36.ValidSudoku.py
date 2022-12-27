"""
https://leetcode.com/problems/valid-sudoku/
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for i in range(9):
            d = {}
            for j in range(9):
                if board[i][j] == ".":
                    pass
                elif board[i][j] in d:
                    return False
                else:
                    d[board[i][j]] = True
        # columns
        for j in range(9):
            d = {}
            for i in range(9):
                if board[i][j] == ".":
                    pass
                elif board[i][j] in d:
                    return False
                else:
                    d[board[i][j]] = True
        # check sub-boxes
        for m in range(0, 9, 3):
            for n in range(0, 9, 3):
                d = {}
                for i in range(n, n+3):
                    for j in range(m, m+3):
                        if board[i][j] == ".":
                            pass
                        elif board[i][j] in d:
                            return False
                        else:
                            d[board[i][j]] = True
        return True