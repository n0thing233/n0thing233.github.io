# 非套路题，细节实现题。。。
# 关键点是： 一旦发现q没东西了 才read4....
class Solution:
    def __init__(self):
        self.q = collections.deque()
    def read(self, buf: List[str], n: int) -> int:
        buf4 = [' ' for i in range(4)]
        idx = 0
        while idx != n:
            if not self.q:
                count = read4(buf4)
                if count == 0:
                    return idx
                for i in range(count):
                    self.q.append(buf4[i])
            while self.q and idx != n:
                buf[idx] = self.q.popleft()
                idx += 1
        return idx   
