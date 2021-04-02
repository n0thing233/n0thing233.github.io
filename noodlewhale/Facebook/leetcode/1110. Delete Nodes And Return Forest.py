class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return
        self.res = []
        def helper(node,parent_deleted):
            if not node:
                return
            if node.val not in to_delete and parent_deleted:
                self.res.append(node)
            parent_deleted = True if node.val in to_delete else False
            node.left = helper(node.left,parent_deleted)
            node.right = helper(node.right,parent_deleted)
            return None if parent_deleted else node
        helper(root,True)
        return self.res
