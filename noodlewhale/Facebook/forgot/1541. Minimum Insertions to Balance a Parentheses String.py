#这题主要理解两点：
#1. 必须连续的)才可以match （
#2. nums表示必须在当前位置解决的(插入)，有可能是(也有可能是） right则后面出现的话可以消掉。nums不能消
#这题非常难！！！！没思路。。。。。
class Solution:
    def minInsertions(self, s: str) -> int:
        nums = right = 0
        for c in s:
            if c == '(':
                #check if ) is odd
                if right%2:
                    nums += 1
                    right -= 1
                right += 2
            else:
                right -= 1
                if right == -1:
                    nums += 1
                    right = 1
        return nums + right
                    
