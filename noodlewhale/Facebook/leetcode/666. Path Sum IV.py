from collections import deque
class Solution:
    def pathSum(self, nums: List[int]) -> int:
        def deserialize(nums):
            q = deque()
            nums_q = deque(nums)
            root_num = nums_q.popleft()
            root_node = TreeNode(root_num%10)
            q.append((root_num,root_node))
            def match_left(a,b):
                return a//100+1 == b//100 and 2*(a%100//10)-1 == b%100//10
            def match_right(a,b):
                return a//100+1 == b//100 and 2*(a%100//10) == b%100//10
            while q:
                num,node = q.popleft()
                if not nums_q:
                    break
                if match_left(num,nums_q[0]):
                    popped = nums_q.popleft()
                    node.left = TreeNode(popped%10)
                    q.append((popped,node.left))
                if not nums_q:
                    break
                if match_right(num,nums_q[0]):
                    popped = nums_q.popleft()
                    node.right = TreeNode(popped%10)
                    q.append((popped,node.right))    
            return root_node            
        root = deserialize(nums)
        if not root:
            return
        self.res = 0
        def get_sum(node,path_sum):
            if not node.left and not node.right:
                self.res += (path_sum+node.val)
            if node.left:
                get_sum(node.left,path_sum+node.val)
            if node.right:
                get_sum(node.right,path_sum+node.val)
        get_sum(root,0)   
        return self.res
