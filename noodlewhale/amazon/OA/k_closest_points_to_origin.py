#O(n*logk)
#O(k)
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for point in points:
            distance = point[0]**2 + point[1]**2
            heapq.heappush(heap,(-distance,point))
            if len(heap) > K:
                heapq.heappop(heap)
        res = [i[1] for i in heap]
        return res
 
