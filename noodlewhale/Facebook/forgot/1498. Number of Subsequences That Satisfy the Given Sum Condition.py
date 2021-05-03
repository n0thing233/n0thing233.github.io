# subsequence == subset 首先要明白顺序不重要
#  排序之后， two pointer就行，左边的点uniquely identify 不同的sequence,所以右边的点有没有都行。
# right < i 就可以直接break了
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        def find_right(right,i,target):
            while right >= i and  nums[right] +nums[i] > target:
                right -= 1
            return right
        n = len(nums)
        right = n-1
        res = 0
        for i in range(n):
            right = find_right(right,i,target)
            if right < i:
                break
            res += (2**(right-i))%(10**9+7)
        return res%(10**9+7)
