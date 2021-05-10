# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#always solve tree problem recursively
#这题还是用recursive思想，对每一个node, 我要怎么reorder left-subttree root 和 right-subtree.
#我需要left_tail 来链接right,我需要right_tail来return给我的parent
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        def helper(node):
            if not node:
                return
            left_tail = helper(node.left)
            right_tail = helper(node.right)
            if not left_tail and not right_tail:
                return node
            elif not left_tail:
                return right_tail
            elif not right_tail:
                node.right = node.left
                node.left = None
                return left_tail
            else:
                left_tail.right = node.right
                node.right = node.left
                node.left = None
                return right_tail
        helper(root)
