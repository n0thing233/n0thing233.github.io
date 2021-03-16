#intuation:brute-force not working pls do compression
#time:O(m*n*k)
#space:O(1)
#bug: wtf 好多bug! matrix转化为row vec 和col vec 每个vec变成一个tuple
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        #do compression
        def multi_matrix(m1,m2):
            m = len(m1)
            k = len(m1[0])
            n = len(m2[0])
            res = [[0 for i in range(n)]for j in range(m)]
            
            #compress m1 to row vectors
            m1_r = []
            for i in range(m):
                row_vec = []
                for j in range(k):
                    if m1[i][j] != 0:
                        row_vec.append((j,m1[i][j]))
                m1_r.append(row_vec)
            
            #compress m2 to col vectors
            m2_c = []
            for i in range(n):
                col_vec = []
                for j in range(k):
                    if m2[j][i] != 0:
                        col_vec.append((j,m2[j][i]))
                m2_c.append(col_vec)
            
            #parewise multi vectors
            for i in range(m):
                for j in range(n):
                    res[i][j] = multi_vectors(m1_r[i],m2_c[j])
            return res
        
        def multi_vectors(v1,v2):
            i = j = 0
            res = 0
            while i < len(v1) and j < len(v2):
                if v1[i][0] < v2[j][0]:
                    i += 1
                elif v1[i][0] > v2[j][0]:
                    j += 1
                else:
                    res += v1[i][1]*v2[j][1]
                    i += 1
                    j += 1
            return res        
        return multi_matrix(mat1,mat2)
