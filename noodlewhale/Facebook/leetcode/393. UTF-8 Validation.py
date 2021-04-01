class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i = 0
        left = 0
        n = len(data)
        def check(left,i,n,data):
            while i < n and left > 0:
                if data[i] >> 6 != 2:
                    return False
                left -= 1
                i += 1
            if left != 0:
                return False
            return True
        while i < n:
            if data[i] >> 7 == 0:
                i += 1
                continue
            elif data[i] >> 6 == 2:
                return False
            elif data[i] >> 3 == 30:
                left = 3
                i += 1
                if not check(left,i,n,data):
                    return False
                i += left
            elif data[i] >> 4 == 14:
                left = 2
                i += 1
                if not check(left,i,n,data):
                    return False
                i += left
            elif data[i] >> 5 == 6:
                left = 1
                i += 1
                if not check(left,i,n,data):
                    return False
                i += left
            else:
                return False
        return True
