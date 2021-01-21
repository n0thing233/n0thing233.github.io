#https://leetcode.com/problems/is-graph-bipartite/
#intuation:start from idnex 0 traverse the graph, if break then return False, else return True
#O(V+E)
#O(V)
from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [-1]*n
        for i in range(n):
            if visited[i] != -1:
                continue
            else:
                queue = deque()
                queue.append((i,0))
                visited[i] = 0
                while queue:
                    curr,flag = queue.popleft()
                    #figure out the logic later
                    for j in graph[curr]:
                        if visited[j]  == -1:
                            queue.append((j, abs(1-flag)))
                            visited[j] = abs(1-flag)
                        elif visited[j] == flag:
                            return False
        return True
