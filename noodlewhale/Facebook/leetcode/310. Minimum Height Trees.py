#center of graph
#topological sort outside to inside
#有意思,还挺tricky的，topological sort 有点像bfs
#最后返回只能是一个或者两个元素
from collections import defaultdict,deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        neighbor = defaultdict(list)
        indegree  = [0 for i in range(n)]
        for edge in edges:
            a = edge[0]
            b = edge[1]
            neighbor[a].append(b)
            neighbor[b].append(a)
            indegree[a] += 1
            indegree[b] += 1
            
        leafs = [i for i in range(n) if indegree[i] == 1]
        q = deque(leafs)
        while q:
            level_length = len(q)
            q_backup = list(q)
            new_level = set()
            for _ in range(level_length):
                popped = q.popleft()
                for node in neighbor[popped]:
                    if indegree[node] != 1:
                        indegree[node] -= 1
                        if indegree[node] == 1:
                            new_level.add(node)                  
            if not new_level:
                return q_backup
            q = deque(new_level)
