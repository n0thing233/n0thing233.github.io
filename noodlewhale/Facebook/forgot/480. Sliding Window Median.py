#two heaps + hashmap with lazy delete
#关键点就是实际上两个heap存多少element 没关系，因为有些已经是deleted,而count是有关系的。
#9:00 9:34 把lazy delete放在rebalance里面，多放几个无所谓。
#time: O(n*log(k))
#space: O(n)
import heapq
from collections import defaultdict
class Solution:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.max_count = 0
        self.min_count = 0
        self.to_be_deleted = defaultdict(int)
    def add(self,num):
        if not self.min_heap:
            heapq.heappush(self.min_heap,num)
            self.min_count += 1
        elif num >= self.min_heap[0]:
            heapq.heappush(self.min_heap,num)
            self.min_count += 1
        else:
            heapq.heappush(self.max_heap,-num)
            self.max_count += 1
    def delete(self,num):
        if num >= self.min_heap[0]:
            self.min_count -= 1
            self.to_be_deleted[num] += 1
        else:
            self.max_count -= 1
            self.to_be_deleted[num] += 1
    def rebalance(self):
        while self.max_count < self.min_count - 1 or self.max_count > self.min_count:
            self.pop_deleted()
            if self.max_count < self.min_count - 1:
                heapq.heappush(self.max_heap,-heapq.heappop(self.min_heap))
                self.min_count -= 1
                self.max_count += 1
            if self.max_count > self.min_count:
                heapq.heappush(self.min_heap,-heapq.heappop(self.max_heap))
                self.max_count -= 1
                self.min_count += 1
        self.pop_deleted()
    def pop_deleted(self):
        while self.min_heap and self.min_heap[0] in self.to_be_deleted:
            popped = heapq.heappop(self.min_heap)
            self.to_be_deleted[popped] -= 1
            if self.to_be_deleted[popped] == 0:
                del self.to_be_deleted[popped]
        while self.max_heap and -self.max_heap[0] in self.to_be_deleted:
            popped = heapq.heappop(self.max_heap)
            self.to_be_deleted[-popped] -= 1
            if self.to_be_deleted[-popped] == 0:
                del self.to_be_deleted[-popped]
    def get_median(self):
        if self.min_count == self.max_count:
            return (self.min_heap[0] - self.max_heap[0])/2
        else:
            return self.min_heap[0]
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if not nums:
            return []
        n = len(nums)
        if k > len(nums):
            return []
        res = []
        for i in range(k):
            self.add(nums[i])
        self.rebalance()
        res.append(self.get_median())
        for i in range(k,n):
            self.add(nums[i])
            self.delete(nums[i-k])
            self.rebalance()
            res.append(self.get_median())
        return res
            
