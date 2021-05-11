class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ''
        data = []
        def helper(root):
            if not root:
                return
            data.append(str(root.val))
            helper(root.left)
            helper(root.right)
            return
        helper(root)
        return ','.join(data)
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return
        data = collections.deque([int(i) for i in data.split(',')])
        def helper(data,l,r):
            val = data.popleft()
            node = TreeNode(val)
            if data and l < data[0] < val:
                node.left = helper(data,l,val)
            if data and val < data[0] < r:
                node.right = helper(data,val,r)
            return node
        return helper(data,float('-inf'),float('inf'))
