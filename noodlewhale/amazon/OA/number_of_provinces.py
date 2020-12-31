#https://leetcode.com/problems/number-of-provinces/submissions/
#time:O(n**2)
#space:O(n**2)
from collections import deque 
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        neighbors = {}
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    if i not in neighbors:
                        neighbors[i] = [j]
                    else:
                        neighbors[i].append(j)
        provinces = 0
        visited = [0 for i in range(n)]
        for i in range(n):
            if visited[i] == 1 :
                continue
            else:
                provinces += 1
                queue = deque()
                queue.append(i)
                while queue:
                    cur = queue.pop()
                    if visited[cur] == 1:
                        continue
                    visited[cur] = 1
                    for i in neighbors[cur]:
                        if visited[i] == 0:
                            queue.append(i)
        return provinces
