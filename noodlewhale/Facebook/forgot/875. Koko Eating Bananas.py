#you remember this name and use binary search....
#注意 left 不能是 0 , bug-free好难。。。。
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 
        right = max(piles)
        def can_eat(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
                if hours > h:
                    return False
            return True
            
        while left < right:
            mid = left + (right-left)//2
            if not can_eat(mid):
                left = mid + 1
            else:
                right = mid
        return left
