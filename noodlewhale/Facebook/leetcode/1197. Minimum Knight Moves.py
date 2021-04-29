#phase 1 move as close as possible （optimized bfs 不过要死记硬背 2 ）
#level_length所有candidate求最小然后 取比最小大2的subset+ visited就可以过了
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        q = collections.deque()
        q.append((0,0,0))
        visited = set([(0,0)])
        while q:
            level_length = len(q)
            dists = []
            for _ in range(level_length):
                a,b,steps = q.popleft()
                if (a,b) == (x,y):
                    return steps              
                for k in [[2,1],[1,2],[1,-2],[-1,2],[2,-1],[-2,1],[-2,-1],[-1,-2]]:
                    i =  a + k[0]
                    j = b + k[1]
                    if (i,j) not in visited:
                        visited.add((i,j))
                        dists.append((i,j,abs(i-x)+abs(j-y)))
            dists = sorted(dists,key = lambda x : x[2])
            for dist in dists:
                if dist[2] - dists[0][2] > 2:
                    break
                q.append((dist[0],dist[1],steps+1))
            
                    
