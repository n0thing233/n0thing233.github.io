#similar to LIS,but two dimension
#dp[i][diff] is length of  arithmetic subsequence ending with i and diff with diff
#dp[i] can be a dictionary
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp =  [{} for i in range(n)]
        dp[0] = {}
        
        res = 1
        for i in range(1,n):
            for j in range(i):
                diff = A[i] - A[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2
                res = max(res,dp[i][diff])
        return res
