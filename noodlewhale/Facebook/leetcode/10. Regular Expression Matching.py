#top-down dp
#好多坑，is_equal很重要（不是你自己的想法所以写起来就忘了）
from functools import lru_cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def is_empty(p,idx_p):
            p_sub = p[idx_p:]
            for i in range(len(p_sub)):
                if i%2 == 1:
                    if p_sub[i] != '*':
                        return False
            return len(p_sub)%2 ==0
        def is_equal(a,b):
            if "." in [a,b]:
                return True
            return a == b
        
        @lru_cache
        def helper(s,p,idx_s,idx_p):
            #base cases
            if idx_s == len(s) and idx_p == len(p):
                return True
            elif idx_s == len(s):
                return is_empty(p,idx_p)
            elif idx_p == len(p):
                return False
            
            #non-base cases
            if idx_p +1 < len(p) and p[idx_p+1] == '*':
                if is_equal(s[idx_s],p[idx_p]):
                    a = helper(s,p,idx_s,idx_p+2)
                    b = helper(s,p,idx_s+1,idx_p)
                    return a or b
                else:
                    return helper(s,p,idx_s,idx_p+2)
            elif is_equal(s[idx_s],p[idx_p]):
                return helper(s,p,idx_s+1,idx_p+1)
            else:
                return False
        return helper(s,p,0,0)
            
