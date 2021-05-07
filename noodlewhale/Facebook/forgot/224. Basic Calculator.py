#这个不行啊。。。卧槽
#用stack
#遇到左括号，res和op 入站
#遇到右括号，处理一下 然后 连续出战
#return 再处理一下
#我tm要吐了。。。。。
class Solution:
    def calculate(self, s: str):
        stack = []
        res = 0
        i = 0       
        sign = 1
        num = 0
        s = s.replace(" ",'')
        n = len(s)
        while i < n:
            c = s[i]
            if c.isdigit():
                num = int(c)
                while i + 1 < n and s[i+1].isdigit():
                    num = 10 * num + int(s[i+1])
                    i += 1
            elif c == '+':
                res += sign*num
                sign = 1
                num = 0
            elif c == '-':
                res += sign*num
                sign = -1
                num = 0
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            else:
                res += sign*num
                res = res * stack.pop()
                res += stack.pop()
                num = 0
            i += 1
        return res + sign*num
