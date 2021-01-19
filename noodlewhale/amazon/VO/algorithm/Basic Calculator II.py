#https://leetcode.com/problems/basic-calculator-ii/submissions/
#入栈操作只处理乘除
#出栈操作处理加减
#truncate towards zero is tricky here,just use int (a/b) will truncate towards zero
#time:O(n)
#space:O(n)
from collections import deque
import math
class Solution:
    def calculate(self, s: str) -> int:
        s = s.strip().replace(' ','')
        n = len(s)
        curr_number = 0
        last_operator = '+'
        stack = deque()
        for i in s:
            #print(stack)
            if i not in ['+','-','*','/']:
                curr_number  = curr_number*10 + int(i)
            else:
                if last_operator in ['+','-']:
                    stack.append(curr_number if last_operator == '+' else -curr_number)
                elif last_operator == '*':
                    last_number = stack.pop()
                    new_number = last_number*curr_number
                    stack.append(new_number)
                else:
                    last_number = stack.pop()
                    new_number = int(last_number/curr_number)
                    stack.append(new_number)                        
                last_operator = i
                curr_number = 0
        #print(last_operator)
        #print(curr_number)
        if last_operator in ['+','-']:
            stack.append(curr_number if last_operator == '+' else -curr_number)
        elif last_operator == '*':
            last_number = stack.pop()
            new_number = last_number*curr_number
            stack.append(new_number)
        else:
            last_number = stack.pop()
            new_number = int(last_number/curr_number)
            stack.append(new_number)
        res = 0
        while stack:
            res += stack.pop()
        return res
