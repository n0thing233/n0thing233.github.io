#最优解不用reverse还是要记一下
#10:16 10:27
#两个bug : 1.不用reverse,因为你就是反着build的。2.转化为int后要再转回str
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        l1 = len(num1)
        l2 = len(num2)
        res = [0 for i in range(l1+l2-1)]
        for i in range(l1):
            for j in range(l2):
                res[i+j] += int(num1[i])*int(num2[j])
        carry = 0
        for i in range(l1+l2-2,-1,-1):
            carry,res[i] = divmod(res[i]+carry,10)
        if carry:
            res = [carry] + res
        return ''.join(([str(i) for i in res]))
