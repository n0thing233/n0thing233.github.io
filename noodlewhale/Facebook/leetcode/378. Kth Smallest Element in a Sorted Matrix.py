#intuation: Im not goign to learn binary search approach
#time:  O(log(min(k,n))) + Klog(MIN(k,n))
#space: O(k)
#bug:. while循环忘记 -1了
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:
            return
        min_heap = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(min(k,m)):
            heapq.heappush(min_heap,(matrix[i][0],i,0))
        while k > 1:
            _,row,col = heapq.heappop(min_heap)
            if col < n-1:
                heapq.heappush(min_heap,(matrix[row][col+1],row,col+1))
            k -= 1
        return min_heap[0][0]
