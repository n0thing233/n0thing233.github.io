#recursive不是那么好想，直接上interative inorder traverse 已经pop 的node 左孩子用不上了，作为prev的时候有孩子也用不上了所以可以更改
#用stack啊同学，不是queue
from collections import deque
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        stack = []
        if not root:
            return
        dummy = Node()
        prev = dummy
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            node.left = prev
            prev.right = node
            prev = node
            node = node.right
        
        prev.right = dummy.right
        dummy.right.left = prev
        return dummy.right
