#1.最核心的idea就是两个stack,其中operator stack 是monotonic 的。
#2.其次要处理 减号作为unary operator,插入number后 uniary变为False,插入 +-*/后unary变为true
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ','')
        operators = []
        operands =[]
        def calculate(operators,operands):
            a = operands.pop()
            b = operands.pop()
            c = operators.pop()
            if c == '+':
                return a+b
            elif c == '-':
                return b-a
            elif c == '*':
                return a*b
            else:
                return int(b/a)
        priorities = {
            "(": -1,
            ")": -1,
            "+": 0,
            "-": 0,
            "*": 1,
            "/": 1          
        }
        
        #using while because i can go more than 1 step in one interation
        i = 0
        n = len(s)
        
        #handle "-" as unary operator
        is_unary = True
        while i < n:
            if (s[i] == '-' and is_unary) or s[i].isdigit():
                sign = 1
                if s[i] == '-':
                    sign = -1
                    i += 1
                number = int(s[i])
                while i+1 < n and s[i+1].isdigit():
                    number = number*10 + int(s[i+1])
                    i += 1
                operands.append(sign*number)
                is_unary = False
            elif s[i] == "(":
                operators.append(s[i])
                is_unary = True
            elif s[i] == ")":
                while operators[-1] != '(':
                    operands.append(calculate(operators,operands))
                operators.pop()
                #is_unary = True
            else:
                while operators and priorities[s[i]] <= priorities[operators[-1]]:
                    operands.append(calculate(operators,operands))
                operators.append(s[i])
                is_unary = True
            i += 1
        while operators:
            operands.append(calculate(operators,operands))
        return operands[0]
                
