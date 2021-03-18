#comment: heapq不行的，必须quickselect
#吭哧吭哧写出了一个quickselect? O(n)
import random
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.res = []
        def get_distance(point):
            return point[0]**2+point[1]**2
        n = len(points)
        def get_pivot(points,start,end,k):
            pivot = random.randint(start,end)
            points[start],points[pivot] = points[pivot],points[start]
            index = start + 1
            for i in range(start+1,end+1):
                if get_distance(points[i]) > get_distance(points[start]):
                    continue
                else:
                    points[i],points[index] = points[index],points[i]
                    index += 1
            points[index-1],points[start] = points[start],points[index-1]
            return index-1
        def quickselect(points,start,end,k):
            pivot = get_pivot(points,start,end,k)
            if pivot == k:
                return
            elif pivot < k:
                quickselect(points,pivot,end,k)
            else:
                quickselect(points,start,pivot,k)
        quickselect(points,0,n-1,k-1) 
        return points[:k]
