# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#recursive, is_left_bst, node, num, largest, lowest
#           is_right_bst,num,largest,lowest
#bottom-up is enough...
#float('inf')方法太巧妙了。。还是用自己的方法实现一遍吧。。
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = None
        self.num = float('-inf')
        def helper(node):
            if not node:
                return True,0,float('inf'),float('-inf')
            is_bst_l,num_l,min_l,max_l = helper(node.left)
            is_bst_r,num_r,min_r,max_r = helper(node.right)
            if is_bst_l and is_bst_r:
                if max_l < node.val < min_r:
                    if num_l+num_r+1 > self.num:
                        self.num = num_l+num_r+1
                        self.res = node
                    return True,num_l+num_r+1,min(node.val,min_l), max(node.val,max_r)
                else:
                    return False,None,None,None
            else:
                return False,None,None,None 
        helper(root)
        return self.num
