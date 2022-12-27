"""
https://leetcode.com/problems/spiral-matrix-ii/
"""

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        while matrix:
            top = left = 0
            right = n - 1
            bottom = n - 1
            num = 1
            matrix = []
            while top <= bottom and left <= right:
                # top row
                for i in range(left, right + 1):
                    matrix[top][i] = num
                    num += 1
                # right column
                for j in range(top + 1, bottom):
                    matrix[j][right] = num
                    num += 1
                # bottom row
                for i in reversed(range(left, right + 1)):
                    if left < right:
                        matrix[bottom][i] = num
                        num += 1
                # left row
                for j in reversed(range(top, bottom + 1)):
                    if top < bottom:
                        matrix[j][left] = num
                        num += 1
                left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return matrix 
    