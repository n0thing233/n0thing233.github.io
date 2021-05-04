#其实binary search+ dfs/bfs非常直观。但你还是选择dijkistra
#每一步都扩张可以reach的最小的cell. 记录曾经走过的最大值。。。。。死记硬背吧。。
#time:O(n^2logn)
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        min_heap = []
        min_heap.append((grid[0][0],0,0))
        res = 0
        n = len(grid)
        visited = set((0,0))
        while min_heap:
            cost,i,j = heapq.heappop(min_heap)
            res = max(res,cost)
            if i == n-1 and j == n-1:
                return res
            for k in [[0,1],[1,0],[-1,0],[0,-1]]:
                x = i + k[0]
                y = j + k[1]
                if 0 <= x < n and 0 <= y < n and (x,y) not in visited:
                    visited.add((x,y))
                    heapq.heappush(min_heap,(grid[x][y],x,y))
