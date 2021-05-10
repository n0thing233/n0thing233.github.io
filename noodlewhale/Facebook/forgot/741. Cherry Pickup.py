#只记得是两个路径一起走，但记不清怎样implement
#现在记住dp[i][j][u][v]代表第一个人走到i,j 第二个人走到(u,v) 的答案
#求dp[n-1][n-1][n-1][n-1]
from functools import lru_cache
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        memo1 = {}
        memo2 = {}
        def get_available(x,y):
            if (x,y) in memo1:
                return memo1[(x,y)]
            res = []
            if  x-1 >= 0 and grid[x-1][y] != -1:
                res.append([x-1,y])
            if y-1 >= 0 and grid[x][y-1] != -1:
                res.append([x,y-1])
            memo1[(x,y)] = res
            return res        
        def helper(i,j,k):
            if i == j == k == 0:
                return grid[0][0]
            if (i,j,k) in memo2:
                return memo2[(i,j,k)]
            tmp = -1
            for a in get_available(i,j):
                for b in get_available(k,i+j-k):
                    tmp = max(tmp,helper(a[0],a[1],b[0]))
            if tmp == -1:
                memo2[(i,j,k)] = -1
                return tmp
            if i == k:
                tmp += grid[i][j]
            else:
                tmp += (grid[i][j] + grid[k][i+j-k])
            memo2[(i,j,k)] = tmp
            return tmp
        res = helper(n-1,n-1,n-1)
        return max(res,0)
