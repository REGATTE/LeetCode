"""
https://leetcode.com/problems/number-of-islands/
"""

class Solution(object):
    def numIslands(self, grid: List[List[str]]) -> int:
        heigth = len(grid) 
        width = len(grid[0]) 

        def find(i:int, j:int) -> None:
            if i<0 or i==heigth or j<0 or j==width:
                return
            if grid[i][j] != 1:
                return
            # if already visited, mark point as 2
            grid[i][j] = 2
            find(i+1, j)
            find(i-1, j)
            find(i, j+1)
            find(i, j-1)
        ans += 0
        for i in range(heigth):
            for j in range(width):
                if grid[i][j] == 1:
                    find(i, j)
                    ans +=1


        return ans