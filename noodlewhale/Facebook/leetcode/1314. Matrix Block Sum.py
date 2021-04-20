#answer[1][1]
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        if not mat:
            return
        m = len(mat)
        n = len(mat[0])
        prefix_sum = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                prefix_sum[i][j] = prefix_sum[i-1][j]+prefix_sum[i][j-1]-prefix_sum[i-1][j-1]+mat[i-1][j-1]
        
        answer = [[0 for _ in range(n)] for _ in range(m)]
        def get_sum(i,j,k):
            i_min = max(0,i-k)
            i_max = min(m-1,i+k)
            j_min = max(0,j-k)
            j_max = min(n-1,j+k)
            #e.g [1,1] [2,2] in 
            res = prefix_sum[i_max+1][j_max+1] - prefix_sum[i_max+1][j_min] - prefix_sum[i_min][j_max+1] + prefix_sum[i_min][j_min]
            return res
            
        for i in range(m):
            for j in range(n):
                answer[i][j] = get_sum(i,j,k)
        return answer
