#用list表示edge
#
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbors = [[] for i in range(n)]
        visited = [False]*n
        for edge in edges:
            neighbors[edge[0]].append(edge[1])
            neighbors[edge[1]].append(edge[0])
        def dfs(visited, neighbors, i):
            if visited[i]:
                return False
            else:
                visited[i] = True
                for neighbor in neighbors[i]:
                    dfs(visited,neighbors,neighbor)
                return True                
        counter = 0
        for i in range(n):
            if dfs(visited,neighbors,i):
                counter += 1
        return counter
