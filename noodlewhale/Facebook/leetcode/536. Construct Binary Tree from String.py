#1.把string转化为数组，所以才不会被复制
#2. 判断正负号
#3.判断做孩子是否为空
#4.判断数字是否结束
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        s = collections.deque([i for i in s])
        def helper(s):
            #print(s)
            if not s:
                return
            if s[0] == ')':
                return
            sign = 1
            if s[0] == '-':
                sign = -1
                s.popleft()
            num = 0
            while s and s[0].isdigit():
                num = num*10 + int(s[0])
                s.popleft()
            num = num*sign
            node = TreeNode(num)
            if s and s[0] == "(":
                s.popleft()
                node.left = helper(s)
                s.popleft()
            if s and s[0] == '(':
                s.popleft()
                node.right = helper(s)
                s.popleft()
            return node
        return helper(s)
