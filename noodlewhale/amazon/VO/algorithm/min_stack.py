#https://leetcode.com/problems/min-stack/submissions/
#float inf as the defualt getMin
from collections import deque
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = deque()
    def push(self, x: int) -> None:
        if x < self.getMin():
            self.min_stack.append((x,x))
        else:
            self.min_stack.append((x,self.getMin()))

    def pop(self) -> None:
        return self.min_stack.pop()[0]

    def top(self) -> int:
        return self.min_stack[-1][0]

    def getMin(self) -> int:
        if len(self.min_stack) == 0:
            return float('inf')
        return self.min_stack[-1][1]
