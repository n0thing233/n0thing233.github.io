#这题先背下吧。。
#首选想清楚 可不可以overlap,当然可以，目的是求最大cherry
#可以overlap之后把思维转变成两个同时从左上走到右下，有问题吗？ 没问题。。。
#两个人最终都会走 2*n -2步到重点
#dp[i][j][u][v] 代表 第一个人在i,j 第二个人在u,v 的时候，走到终点最多可以摘的树木
#发现i + j = u + v 所以可以去掉一维。意思就是dp[i][j][u]确定唯一的v
#状态转换方程：
#dp[i][j][u]可以从四个状态转换来：dp[i+1][j][u] dp[i][j+1] dp[i+1][j][u+1] dp[i][j+1][u+1]
#base case: u+v == i + j == 2*n -2
#lru_cache out of memory memo is fine.
from functools import lru_cache
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        n = len(grid)
        if -1 in [grid[n-1][n-1],grid[0][0]]:
            return -1
        def is_valid(x,y,z):
            return 0 <= x < n and 0 <= y < n and 0 <= z < n and 0 <= x+y-z < n and grid[x][y] != -1 and grid[z][x+y-z] != -1
        memo = {}
        def helper(i,j,k):
            if i == j == k == n-1:
                return grid[n-1][n-1]
            if (i,j,k) in memo:
                return memo[(i,j,k)]
            res = 0
            res += grid[i][j]
            res += grid[k][i+j-k]
            if i == k:
                res -= grid[i][j]
            gain = -float('inf')
            for l in [[1,0,0],[0,1,0],[1,0,1],[0,1,1]]:
                x = i + l[0]
                y = j + l[1]
                z = k + l[2]
                if is_valid(x,y,z):
                    gain = max(gain,helper(x,y,z))
            memo[(i,j,k)] = res + gain
            return memo[(i,j,k)]
        return max(0,helper(0,0,0))
