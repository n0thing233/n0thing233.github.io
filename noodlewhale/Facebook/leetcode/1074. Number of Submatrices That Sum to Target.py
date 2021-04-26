#先想明白一维的prefix_sum,不用two_sum dictionary,则需要n**2,对每一个subarray起点，对应平均n个终点，
#但用了dictionary,就可以从左到右扫一遍，O(1)时间查看n个.

#同样道理，generalize到2D就变成了，先fix row1,row2(这个是R**2),然后就变成1D扫一遍col所以复杂度是C*(R**2)
#还可以进一步优化。。只求一个dimension的prefix_sum且放在原二维数组中。
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        prefix_sum = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + matrix[i-1][j-1]
        res = 0
        for i in range(n):
            for j in range(i,n):
                sum_dict = {}
                running_sum = 0
                for k in range(m+1):
                    running_sum = (prefix_sum[k][j+1] - prefix_sum[k][i])
                    if running_sum - target in sum_dict:
                        res += sum_dict[running_sum-target]
                    if running_sum in sum_dict:
                        sum_dict[running_sum] += 1
                    else:
                        sum_dict[running_sum] = 1
        return res
                        
