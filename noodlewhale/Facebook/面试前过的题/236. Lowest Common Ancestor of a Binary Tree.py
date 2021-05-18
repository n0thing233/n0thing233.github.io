#LCA 本A..
#套路题。。recursive解决。。
#关键点是只关心找到的count,而不是p 或者q,值得面试前看一下！
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
