#dp入门。。。。其实没有理解
#从pplaylist的最后一个song 入手，还是不是很理解， 背吧。。。。
#dp[i][j] = dp[i-1][j-1]*(N-j+1) + dp[i-1][j]*(j-k)
from functools import lru_cache
class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        @lru_cache
        def helper(i,j):
            #we can use 0 song to fill a 0 playlist
            if i == 0 and j == 0:
                return 1
            elif i == 0:
                return 0
            elif j == 0:
                return 0
            else:
                res = 0
                res += helper(i-1,j-1)*(N-j+1)
                res %= 10**9+7
                res += helper(i-1,j)*max(0,j-K)
                res %= 10**9+7
            return res
        return helper(L,N)
