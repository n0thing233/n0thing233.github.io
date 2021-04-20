#dp 定义难，base case难，target function 难，转换方程难。。。。。
#dp[i][j] = k , k is the index in S so that S[k:i] is the shortest postfix of S and T[:j] is a subsequence of S[k:i]
# what you are looking for is min(i-dp[i][len(T)-1]+1) for i in range(len(S))
# if S[i] == T[j] dp[i][j] = max([dp[k][j-1] for k in range(i-1)])
#      else:    dp[i][j] = -1
#因为还没有完全理解dp,所以以上全部死记硬背
# visualize之后更好理解，先fill 第一行 第一列， 然后竖着fill每一列
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        m = len(S)
        n = len(T)
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        
        #fill the first col
        for i in range(m):
            if S[i] == T[0]:
                dp[i][0] = i
        
        #fill the first row:
        #for j in range(1,n):
        #    dp[0][j] = -1
        
        #fill each col
        for j in range(1,n):
            cur = dp[0][j-1]
            for i in range(1,m):
                if S[i] == T[j]:
                    dp[i][j] = cur
                cur = max(cur,dp[i][j-1])
        
        #find answer
        cur = float('inf')
        ret = ''
        for i in range(m):
            if dp[i][n-1] != -1:
                if i-dp[i][n-1]+1 < cur:
                    cur = i-dp[i][n-1]+1
                    ret = S[dp[i][n-1]:(i+1)]
        return ret
