#similar to next permutation
#[::-1]不能用range 下标
class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n-1,0,-1):
            #find left
            if arr[i] < arr[i-1]:
                left = i-1
                #find right:
                right = i
                for j in range(i+1,n):
                    #这个edge case及其tricky.我明白要找恰好小于left的item,但是要找的是第一个occurance
                    if arr[j] < arr[i-1] and arr[j] > arr[j-1]:
                        right = j
                arr[left],arr[right] = arr[right],arr[left]
                return arr
        return arr
