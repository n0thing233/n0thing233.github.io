# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(root,node,path):
            if node == root:
                return path+[node]
            if not root.left and not root.right:
                return
            if root.left:
                left_found = find(root.left,node,path+[root])
                if left_found:
                    return left_found
            if root.right:
                right_found = find(root.right,node,path+[root])
                if right_found:
                    return right_found
        p_path = find(root,p,[])
        q_path = find(root,q,[])
        if len(p_path) > len(q_path):
            p_path,q_path = q_path ,p_path
            p,q = q,p
        n = len(p_path)
        if p_path[n-1] == q_path[n-1]:
            return p
        curr = 0
        for i in range(len(p_path)):
            if p_path[i] != q_path[i]:
                return p_path[i-1]

        
        
            
        
