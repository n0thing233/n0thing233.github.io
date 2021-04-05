# 总结，只需要一开始push_left root,有right就push_left right,只要stack空就是结束！
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        p1 = root1
        p2 = root2
        
        stack1 = []
        stack2 = []
        res = []
        def push_left(node,stack):
            while node:
                stack.append(node)
                node = node.left
        def pop_push(stack):
            node = stack.pop()
            res.append(node.val)
            if node.right:
                push_left(node.right,stack)
            return
        push_left(p1,stack1)
        push_left(p2,stack2)
        while stack1 or stack2:
            #it cannot happen
            if not stack1 and not stack2:
                return
            if not stack1:
                pop_push(stack2)
            elif not stack2:
                pop_push(stack1)
            else:
                if stack1[-1].val >= stack2[-1].val:
                    pop_push(stack2)
                else:
                    pop_push(stack1)
        return res
                    
            
