#注意constraint lower 一定小于nums[0],upper 一定大于nums[i]
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        #find lower_bound and upper_bound
        def get_str(left,right):
            if left == right:
                return str(left)
            else:
                return str(left)+"->"+str(right)
        if not nums:
            return [get_str(lower,upper)]
        res = []
        if lower < nums[0]:
            res.append(get_str(lower,nums[0]-1))
        n = len(nums)
        for i in range(n-1):
            if nums[i] + 1 < nums[i+1]:
                res.append(get_str(nums[i]+1,nums[i+1]-1))
        if nums[-1] < upper:
            res.append(get_str(nums[-1]+1,upper))
        return res
