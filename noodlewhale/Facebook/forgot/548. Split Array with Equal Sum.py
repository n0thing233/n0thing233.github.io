#框架思路想到了，但一边存在多个答案（因为有negative存在）忘记了，需要放到set里
#9:45
#time:O(n**2)
#space:O(n)
class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        if not nums:
            return False
        n = len(nums)
        prefix_sum = [0 for i in range(n+1)]
        for i in range(1,n+1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
        
        #fix mid and check left and right
        for i in range(3,n-3):
            tmp = set()
            #traverse left
            for j in range(1,i-1):
                if prefix_sum[j] == prefix_sum[i] - prefix_sum[j+1]:
                    tmp.add(prefix_sum[j])
            for k in range(i+2,n-1):
                if prefix_sum[k] - prefix_sum[i+1] == prefix_sum[n] - prefix_sum[k+1]:
                    if prefix_sum[k] - prefix_sum[i+1] in tmp:
                        return True
        return False
