from typing import List
from collections import deque
class Solution:
    def openLock(self, deadends:List[str], target: str) -> int:
        queue  = deque()
        queue.append("0000")
        board = [[[[0 for i in range(10)] for j in range(10)] for k in range(10)] for l in range(10)]
        while queue:
            node = queue.popleft()
            #print("primary node:")
            #print(node)
            q = int(node[0])
            w = int(node[1]) 
            e = int(node[2]) 
            r = int(node[3])
            if node == target:
                return board[q][w][e][r]
            if node in deadends:
                continue;
            offset_list = [[1,0,0,0],[-1,0,0,0],[0,1,0,0],[0,-1,0,0],[0,0,1,0],[0,0,-1,0],[0,0,0,1],[0,0,0,-1]]
            for k in offset_list:
                a = (q+k[0])%10
                b = (w+k[1])%10
                c = (e+k[2])%10
                d = (r+k[3])%10
                if board[a][b][c][d]!= 0 :
                    continue;
                node_new = str(a)+str(b)+str(c)+str(d)               
                board[a][b][c][d] = board[q][w][e][r]+1
                #print(node_new)
                #print(board[a][b][c][d])
                queue.append(node_new)
            
        return -1      
            
        
