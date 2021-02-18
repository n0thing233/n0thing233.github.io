#232. https://leetcode.com/problems/implement-queue-using-stacks/submissions/
# all operations O(1). lazy load
from collections import deque
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_1 = deque()
        self.stack_2 = deque()
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_1.append(x)
        return

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.stack_2) > 0:
            return self.stack_2.pop()
        elif len(self.stack_1) == 0:
            raise Exception("Sorry, no element to pop")
        else:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
            return self.stack_2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.stack_2) > 0:
            return self.stack_2[-1]
        elif len(self.stack_1) == 0:
            raise Exception("Sorry, no element in stack")
        else:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
            return self.stack_2[-1]
        
        
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.stack_1) == 0 and len(self.stack_2) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
