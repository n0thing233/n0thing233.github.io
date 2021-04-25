#太巧妙了。。先死记硬背吧。。。。
from bisect import bisect_left as bl,bisect_right as br
class RangeModule:

    def __init__(self):
        self._list = []
        
    def addRange(self, left: int, right: int) -> None:
        #bl(left) is odd, br(right) is odd - > not insert left & not insert right, remove everything between
        #bl(left) is odd, br(right) is even - > not insert left & insert right, remove everything between
        #bl(left) is even, br(right) is odd - > insert left & not insert right, remove everythin between
        #bl(left) is even, br(right) is even - > insert left & insert right, remove everything between
        i = bl(self._list,left)
        j = br(self._list,right)
        self._list[i:j] = [left]*(i%2 == 0) + [right]*(j%2 == 0)

    def queryRange(self, left: int, right: int) -> bool:
        i = br(self._list,left)
        j = bl(self._list,right)
        return i == j and i%2 == 1

    def removeRange(self, left: int, right: int) -> None:
        #simialr to addrange
        i = bl(self._list,left)
        j = br(self._list,right)
        self._list[i:j] = [left]*(i%2 == 1) + [right]*(j%2 == 1)

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right    `1)
