#median fo stream + hashmap
#time:n*(logk)
import heapq
class Solution:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.min_count = 0
        self.max_count = 0
        self.deleted = {}
    def rebalance(self):
        while self.max_count < self.min_count -1 or self.max_count > self.min_count:
            if self.max_count  < self.min_count - 1:
                heapq.heappush(self.max_heap,-heapq.heappop(self.min_heap))
                self.max_count += 1
                self.min_count -= 1
            elif self.max_count > self.min_count:
                heapq.heappush(self.min_heap,-heapq.heappop(self.max_heap))
                self.min_count += 1
                self.max_count -= 1
        return
    def pop_deleted(self):
        while self.min_heap and self.min_heap[0] in self.deleted:
            popped = heapq.heappop(self.min_heap)
            self.deleted[popped] -=1 
            if self.deleted[popped] == 0:
                del self.deleted[popped]
        while self.max_heap and -self.max_heap[0] in self.deleted:
            popped = -heapq.heappop(self.max_heap)
            self.deleted[popped ] -= 1
            if self.deleted[popped] == 0:
                del self.deleted[popped]
        return
    def add_num(self,num):
        if not self.min_heap:
            heapq.heappush(self.min_heap,num)
            self.min_count += 1
        elif num >= self.min_heap[0]:
            heapq.heappush(self.min_heap,num)
            self.min_count += 1
        else:
            heapq.heappush(self.max_heap,-num)
            self.max_count += 1
    def delete_num(self,num):
        if self.min_heap and num >= self.min_heap[0]:
            self.min_count -= 1
        else:
            self.max_count -= 1
        if num not in self.deleted:
            self.deleted[num] = 1
        else:
            self.deleted[num] += 1
        return
    def get_median(self):
        if self.max_count == self.min_count - 1:
            return self.min_heap[0]
        else:
            return (-self.max_heap[0]+self.min_heap[0])/2
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if not nums or len(nums) < k:
            return []
        n = len(nums)
        for i in range(k):
            self.add_num(nums[i])
        self.rebalance()
        res = []
        res.append(self.get_median())
        for i in range(k,n):
            self.add_num(nums[i])
            self.delete_num(nums[i-k])
            self.rebalance()
            self.pop_deleted()
            res.append(self.get_median())
        return res
