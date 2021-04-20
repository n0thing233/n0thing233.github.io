#这种类型题还挺灵活的，并不是一定一种解法。
#有些适合sweep line,有些适合stack有些就是greedy.
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points,key = lambda x: x[1])
        res = 1
        cur_end = points[0][1]
        for point in points[1:]:
            s = point[0]
            e = point[1]
            if s > cur_end:
                res += 1
                cur_end = e
        return res
