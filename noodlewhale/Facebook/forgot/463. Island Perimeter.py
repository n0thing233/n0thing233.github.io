#9:30 9:45写出来但是需要debug
#第一次遇到的bug,break并不能break两个 for loop. 应该直接return
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.res = 0
        m = len(grid)
        n = len(grid[0])
        visited = set()
        
        def dfs(i,j):
            visited.add((i,j))
            count = 0
            for k in [[1,0],[0,1],[-1,0],[0,-1]]:
                x = i + k[0]
                y = j + k[1]
                if 0 <= x < m and 0 <= y < n:
                    if grid[x][y] == 1:
                        count += 1
                        if not (x,y) in visited:
                            dfs(x,y)
            self.res += (4-count)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i,j)
                    return self.res
