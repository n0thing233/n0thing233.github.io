class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        parent = {}
        def find_k(node):
            if not node:
                return
            if node.right:
                parent[node.right] = node
            if node.left:
                parent[node.left] = node
            if node.val == k:
                return node
            res_left = find_k(node.left)
            if res_left:
                return res_left
            res_right = find_k(node.right)
            if res_right:
                return res_right
            return None
        def bfs(node):
            visited = set()
            visited.add(node.val)
            q = collections.deque()
            q.append(node)
            while q:
                popped = q.popleft()
                if not popped.left and not popped.right:
                    return popped.val
                if popped.left and popped.left not in visited:
                    visited.add(popped.left)
                    q.append(popped.left)
                if popped.right and popped.right not in visited:
                    visited.add(popped.right)
                    q.append(popped.right)
                if popped in parent and parent[popped] not in visited:
                    visited.add(parent[popped])
                    q.append(parent[popped])
        node = find_k(root)
        res = bfs(node)    
        return res
