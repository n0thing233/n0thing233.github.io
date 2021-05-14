#唏嘘感慨，6年前写出最优解的你，在2018和2020年都没有写出最优解。。。
#现在年纪大了，又要追求最优解了！！！
#space:O(1)
#两个tricky点：
#1. 向右走向下走可以直接走。
#2. 向左走，向上走需要判断当前row,col是不是已经走过了。
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        start_row = 0
        end_row = m-1
        start_col = 0
        end_col = n-1
        res = []
        while start_row <= end_row and start_col<= end_col:
            #execute this no matter what...
            for i in range(start_col,end_col+1):
                res.append(matrix[start_row][i])
            start_row +=1
            for i in range(start_row,end_row+1):
                res.append(matrix[i][end_col])
            end_col -= 1
            if start_row <= end_row:
                for i in range(end_col,start_col-1,-1):
                    res.append(matrix[end_row][i])
                end_row -= 1
            if start_col <= end_col:
                for i in range(end_row,start_row-1,-1):
                    res.append(matrix[i][start_col])
                start_col += 1
        return res
