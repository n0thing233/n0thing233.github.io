#26个字母枚举思想。。。
#sliding 26 ci
#26*O(n)
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
            return
        n = len(s)
        if n < k:
            return 0
        res = 0
        #26 letters
        for h in range(1,27):
            letters = [0 for i in range(26)]
            l = 0
            d = 0
            e_k = 0
            for r in range(n):
                if letters[ord(s[r])-ord('a')] == 0:
                    d += 1
                letters[ord(s[r])-ord('a')] += 1
                if letters[ord(s[r])-ord('a')] == k:
                    e_k += 1
                while d > h:
                    letters[ord(s[l])-ord('a')] -= 1
                    if letters[ord(s[l])-ord('a')] == k-1:
                        e_k -= 1
                    if letters[ord(s[l])-ord('a')] == 0:
                        d -= 1
                    l += 1
                if d == h and e_k == h:
                    res = max(res,r-l+1)
        return res
