#2:37
#bfs or dfs brute force, dijkstra to optimze
#二维greedy最小 纪录最大，或者greedy最大，记录最小，考虑dijkistra
#time:O(m*n*log(m*n))
import heapq
class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        if not A:
            return
        def is_valid(x,y):
            return 0 <= x < R and 0 <= y < C
        R  = len(A)
        C = len(A[0])
        max_heap = []
        max_heap.append((-A[0][0],0,0))
        #using True here because it is gurantee to reach the end point
        res = float('inf')
        visited = set()
        visited.add((0,0))
        while True:
            value,i,j = heapq.heappop(max_heap)
            res = min(res,-value)
            if i == R-1 and j == C-1:
                return res
            for k in [[0,1],[1,0],[-1,0],[0,-1]]:
                x = i + k[0]
                y = j + k[1]
                if is_valid(x,y) and (x,y) not in visited:
                    visited.add((x,y))
                    heapq.heappush(max_heap,(-A[x][y],x,y))
