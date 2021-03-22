#另外一种思路比较难理解，先用dijkistra吧，每次只取增量最小，记录visited
#time:k*m*log(m*n)
#space:O(m*n*m)
import heapq
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m = len(mat)
        n = len(mat[0])
        raw_sum = sum([mat[i][0] for i in range(m)])
        raw_index = tuple([0 for i in range(m)])
        min_heap = [(raw_sum,raw_index)]
        visited = set()
        visited.add(raw_index)
        for j in range(k):
            curr_sum,curr_index = heapq.heappop(min_heap)
            curr_index_list = list(curr_index)
            for i in range(m):
                if curr_index_list[i] + 1 < n :
                    curr_index_list[i] += 1
                    new_index = tuple(curr_index_list)
                    curr_index_list[i] -= 1
                    new_sum = curr_sum - mat[i][curr_index[i]] + mat[i][curr_index[i]+1]
                    if new_index in visited:
                        continue
                    visited.add(new_index)
                    heapq.heappush(min_heap,(new_sum,new_index))
        return curr_sum
