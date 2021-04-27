#只用lock实现的话，相当于同时只有一个thread可以操作这个queue,但事实上一个完美的实现是我们想让很多thread同时
#明显不能直接用queue,至少要自己实现一个blocking的logic
#从题目可以看出来要实现两个功能：1.bounded.2 blocking
from threading import Semaphore
from time import time
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.q = collections.deque()
        self.capacity = capacity
        self.count = 0
        self.e_s = Semaphore(capacity)
        self.d_s = Semaphore(0)
    def enqueue(self, element: int) -> None:
        self.e_s.acquire()
        self.q.append(element)
        self.d_s.release()
    def dequeue(self) -> int:
        self.d_s.acquire()
        res = self.q.popleft()
        self.e_s.release()
        return res
    def size(self) -> int:
        return len(self.q)
