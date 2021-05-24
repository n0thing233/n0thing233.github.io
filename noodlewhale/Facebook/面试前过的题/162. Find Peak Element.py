#一定存在peak element 因为 两边都是负无穷
#还是要死记硬背。。首先比较一边就够了，either mid+1 or mid-1 为什么mid +1 因为mid最大可以等于n-2
#这种题最难！
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left ,right = 0, n-1
        while left < right:
            mid = left + (right- left)//2
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left
