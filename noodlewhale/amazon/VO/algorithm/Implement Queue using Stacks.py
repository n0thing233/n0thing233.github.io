#232. Implement Queue using Stacks
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
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())
        self.stack_1.append(x)
        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())
        return

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            raise Exception("no element to pop")
        return self.stack_1.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            raise Exception("no element in queue")
        return self.stack_1[-1]
        
        
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.stack_1) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
