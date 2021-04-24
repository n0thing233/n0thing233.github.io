#两种思路：先建立k个 sum,在 backtracking里面for each k, 走到index结束返回true
#         找到一个sum/k就 k--,每个for loop都是整个数组，最后k == 1 返回true
#总的来说都是backtracking,第一种更容易理解吧。。
#三点：  1. edge case
#        2. bucket 思想
#        3. 2个关键optimization
# time complexity: n^k
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        #edge case
        if k == 1 or all([num == 0 for num in nums]):
            return True
        if total_sum < k or total_sum%k != 0 :
            return False
        target = total_sum//k
        n = len(nums)
        buckets = [0 for i in range(k)]
        visited = set()
        #critical optimization
        nums = sorted(nums,reverse = True)
        def backtracking(idx):
            if idx == n:
                return len(set(buckets)) == 1 and buckets[0] == target 
            for i in range(k):
                buckets[i] += nums[idx]
                if buckets[i] <= target:
                    if backtracking(idx+1):
                        return True
                buckets[i] -= nums[idx]
                #critical optimization,because it will always try to fill previous buckets
                if buckets[i] == 0:
                    break
            return False
        return backtracking(0)
