#各种调bug.. return new length 而不是index.
class Solution:
    def compress(self, chars: List[str]) -> int:
        p1,p2 = 0,0
        n = len(chars)
        while p2 < n:
            c = chars[p2]
            chars[p1] = c
            p1 += 1
            count = 1
            while p2 + 1 < n and chars[p2+1] == chars[p2]:
                count += 1
                p2 += 1
            if count != 1:
                for i in str(count):
                    chars[p1] = i
                    p1 += 1
            p2 += 1
        return p1
