#看了答案才会，但调不出bug.......bug找到了 lien 16 should be vec[i]-1 not vec[i-1]
#time:    m*k*log(m*k)
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m = len(mat)
        n = len(mat[0])
        min_heap = [(sum([mat[i][0] for i in range(m)]),[0 for i in range(m)])]
        visited = set(tuple(min_heap[0][1]))
        while k > 0:
            cur_sum,vec = heapq.heappop(min_heap)
            for i in range(m):
                if vec[i] == n-1:
                    continue
                vec[i] += 1
                if not tuple(vec) in visited:
                    visited.add(tuple(vec))
                    heapq.heappush(min_heap,(cur_sum - mat[i][vec[i]-1] + mat[i][vec[i]], vec[:]))
                vec[i] -= 1
            k -= 1
        return cur_sum
