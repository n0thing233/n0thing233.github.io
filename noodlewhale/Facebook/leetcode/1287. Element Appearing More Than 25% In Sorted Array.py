#the integer has to be one of 25% index, 50% index, 75% index
# 因为已经int了，所以不用-1
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if not arr:
            return
        n = len(arr)
        a,b,c,d = 0,int(0.25*n),int(0.5*n),int(0.75*n)
        def get_most_left(target):
            left, right = 0,n-1
            while left < right:
                mid = left + (right-left)//2
                if arr[mid] < target:
                    left  = mid + 1
                else:
                    right = mid
            return left
        for i in [a,b,c,d]:
            if arr[i] == arr[get_most_left(arr[i])+int(0.25*n)]:
                return arr[i]
        return
#[1,2,3,3]
