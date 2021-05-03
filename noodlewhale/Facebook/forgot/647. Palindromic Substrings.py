#10:12 这么经典的题都忘了，optimal expand from center!
#time: O(n**2)
#space: O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        def expand(a,b):
            count = 0
            while a >= 0 and b < n:
                if s[a] == s[b]:
                    count += 1
                    a -= 1
                    b += 1
                else:
                    break
            return count
        #odd center
        for i in range(n):
            res += expand(i,i)
        #even center
        for i in range(n-1):
            res += expand(i,i+1)
        return res
        
