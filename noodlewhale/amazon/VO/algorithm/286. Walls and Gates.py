#intuation:start from gate do bfs,optimize: start from each gate simoutaneously
from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue = deque()
        m = len(rooms)
        n = len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i,j))
        while queue:
            i,j = queue.popleft()
            offset =  [[0,1],[1,0],[0,-1],[-1,0]]
            for l in offset:
                x = i + l[0]
                y = j + l[1]
                if 0 <= x < m and 0 <= y < n and rooms[x][y] == 2147483647:
                    rooms[x][y] = rooms[i][j] + 1
                    queue.append((x,y))
        return rooms
