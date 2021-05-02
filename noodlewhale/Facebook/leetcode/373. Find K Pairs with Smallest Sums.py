#不会
#解释的最好：https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/209985/python-heap-solution-with-detail-explanation
#首先，two-pointer不能用 很tricky,自己想！
#还是需要一个heap,pop出来后 两边各+1放进heap中！
#为什么work? 因为从heappop出来的pair和是线性递增的！
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_heap = [(nums1[0]+nums2[0],0,0)]
        res = []
        visited = set((0,0))
        while min_heap and k > 0:
            _,i,j = heapq.heappop(min_heap)
            res.append([nums1[i],nums2[j]])
            if i != len(nums1)-1 and (i+1,j) not in visited:
                visited.add((i+1,j))
                heapq.heappush(min_heap,(nums1[i+1]+nums2[j],i+1,j))
            if j != len(nums2)-1 and (i,j+1) not in visited:
                visited.add((i,(j+1)))
                heapq.heappush(min_heap,(nums1[i]+nums2[j+1],i,j+1))
            k -= 1
        return res
        
