from functools import lru_cache
class Solution:
    def __init__(self):
        self.min_moves = float('inf')
    def get_available_lanes(self,o1,o2):
        res = []
        if 1 not in [o1,o2]:
            res.append(1)
        if 2 not in [o1,o2]:
            res.append(2)
        if 3 not in [o1,o2]:
            res.append(3)
        return res
    def minimum_move(self,n,obstacles):
        obstacles.insert(0,-1)
        @lru_cache
        def dfs(lane,row):
            if row == n:
                return 0
            res = float('inf')
            for i in self.get_available_lanes(obstacles[row],obstacles[row+1]):
                if i == lane:
                    res = min(res,dfs(lane,row+1))
                else:
                    res = min(res,dfs(i,row+1)+1)
            return res
        return dfs(2,0)
 
A = Solution()
print(A.minimum_move(3,[2,1,2])) # expect 1
print(A.minimum_move(7, [1,2,3,1,2,3,1]))#expect  6
print(A.minimum_move(1,[2])) #expect 1
print(A.minimum_move(3,[1,2,2])) #expect 1
print(A.minimum_move(3,[2,1,3])) #expect 2
