# bfs not working because follow up is O(1) space
# 每一层看做linked-list,因为已经establish next了。第一层建立第二层，第二层建立第三层
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        node = root
        while node.left:
            most_left = node.left
            while node.next:
                node.left.next = node.right
                node.right.next = node.next.left
            node.left.next = node.right
            node = most_left
        return root
