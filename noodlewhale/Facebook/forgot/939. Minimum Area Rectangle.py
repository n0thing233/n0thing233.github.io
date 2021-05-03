#完全忘了，看答案，太巧妙了！
#对于任意两点，只要能形成rectangle,就查找另外两个定点在不在points里
#time O(n^2)
#space: O(n)
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points_set = set()
        for point in points:
            points_set.add((point[0],point[1]))
        
        #pair-wise check if two points can form a rectangle
        res = float('inf')
        n = len(points)
        for i in range(n):
            x1 = points[i][0]
            y1 = points[i][1]
            for j in range(i+1,n):
                x2 = points[j][0]
                y2 = points[j][1]
                if x1 == x2 or y1 == y2:
                    continue
                if (x1,y2) in points_set and (x2,y1) in points_set:
                    res = min(res,abs(x1-x2)*abs(y1-y2))
        return 0 if res == float('inf') else res
