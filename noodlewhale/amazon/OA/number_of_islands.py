#https://leetcode.com/problems/number-of-islands/submissions/
#O(m*n)
#O(1)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        if not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        counter = 0
        def dfs(grid,i,j,m,n):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0" :
                return False
            grid[i][j] = "0"
            dfs(grid,i+1,j,m,n)
            dfs(grid,i-1,j,m,n)
            dfs(grid,i,j+1,m,n)
            dfs(grid,i,j-1,m,n)                
            return True
            
        for i in range(m):
            for j in range(n):
                if dfs(grid,i,j,m,n):
                    counter += 1
        return counter 
