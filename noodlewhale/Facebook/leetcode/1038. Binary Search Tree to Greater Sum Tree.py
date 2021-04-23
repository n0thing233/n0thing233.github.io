# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#reverse inorder traverse and maintain an runing sum and update on the fly
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        
        stack = []
        node = root
        running_sum = 0
        while node or stack:
            while node:
                stack.append(node)
                node = node.right
            node = stack.pop()
            node.val += running_sum
            running_sum = node.val
            node = node.left
        return root
