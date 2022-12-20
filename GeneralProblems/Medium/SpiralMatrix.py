"""
https://leetcode.com/problems/spiral-matrix/
"""

class Solution:
    def spiralOrder(matrix):
        result = []
        if matrix == []:
            return result
        
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        
        while left <= right and top <= bottom:
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            for i in range(top + 1, bottom):
                result.append(matrix[i][right])
            for j in reversed(range(left, right + 1)):
                if top < bottom:
                    result.append(matrix[bottom][j])
            for i in reversed(range(top + 1, bottom)):
                if left < right:
                    result.append(matrix[i][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
            
        return result
mat = [
    [1, 2, 3],
    [4,5,6],
    [7,8,9]
]
print(Solution.spiralOrder(mat))