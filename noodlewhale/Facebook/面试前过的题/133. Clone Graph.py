#dfs with visited
#难处理的是neighbor.
# 自己不太能做出来,是一个dfs 但带return的。。。
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        def helper(node):
            if not node:
                return
            if node not in visited:
                cloned = Node(val = node.val)
                visited[node] = cloned
                for i in node.neighbors:
                    if i not in visited:
                        cloned.neighbors.append(helper(i))
                    else:
                        cloned.neighbors.append(visited[i])
            return visited[node]
        return helper(node)
