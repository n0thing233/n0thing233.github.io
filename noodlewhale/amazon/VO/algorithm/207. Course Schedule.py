#一遍bug-free
#topological sort, for indegree = 0 ,push to queue ,pop queue , if any node left, then cannot, else can
#time:O(V+E)
#space:O(E+V)
from collections import deque,defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        neighbors = defaultdict(list)
        for i in prerequisites:
            neighbors[i[1]].append(i[0])
        indegree = [0]*numCourses
        for i in range(numCourses):
            if i not in neighbors:
                neighbors[i] = []
            for j in neighbors[i]:
                indegree[j] += 1
        queue = deque()
        for i,j in enumerate(indegree):
            if j == 0:
                queue.append(i)
        num_res = numCourses
        while queue:
            curr = queue.popleft()
            num_res -= 1
            for i in neighbors[curr]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        return True if num_res == 0 else False
