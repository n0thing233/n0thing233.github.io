#审题。。。return the lexicographically smallest one.。。。。
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return
        if 3*k > len(nums):
            return
        k_array = [sum(nums[:k])]
        for i in range(0,len(nums)-k):
            k_array.append(k_array[-1]-nums[i]+nums[i+k])
        dp_left = [0 for i in range(len(k_array))]
        dp_right = [0 for i in range(len(k_array))]
        dp_left[0] = 0
        dp_right[-1] = len(k_array)-1
        for i in range(1,len(k_array)):
            if k_array[i] > k_array[dp_left[i-1]]:
                dp_left[i] = i
            else:
                dp_left[i] = dp_left[i-1]
        for i in range(len(k_array)-2, -1,-1):
            if k_array[i] >= k_array[dp_right[i+1]]:
                dp_right[i] = i
            else:
                dp_right[i] = dp_right[i+1]
                
        max_sum = 0
        res = []
        for mid in range(len(k_array)):
            if mid - k < 0 or mid + k > len(k_array)-1 :
                continue
            cur = k_array[dp_left[mid-k]]+k_array[mid]+k_array[dp_right[mid+k]]
            if cur > max_sum:
                max_sum = cur
                res = [dp_left[mid-k],mid,dp_right[mid+k]]
        return res
