#位操作。。。
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31-1
        if dividend == 0:
            return 0
        if (dividend > 0) == (divisor > 0):
            sign = 1
        else:
            sign = -1
        
        dividend,divisor = abs(dividend),abs(divisor)
        res = 0
        while dividend >= divisor:
            x = divisor
            power = 1
            while dividend >= x :
                x = (x << 1)
                power += 1
            x = (x >> 1)
            power -= 1
            res += 2**(power-1)
            dividend -= x
        return sign*res
