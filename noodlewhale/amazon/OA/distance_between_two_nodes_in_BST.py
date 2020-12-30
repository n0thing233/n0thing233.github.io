#https://leetcode.com/discuss/interview-question/algorithms/125084/amazon-distance-between-2-nodes
#O(logn) if balanced BST
#O(n) worst case
#space O(n)
class TreeNode():
    def __init__(self,val,left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
def get_distance(root,val1,val2):
    list1 = []
    list2 = []
    def get_depth(root,val,my_list):
        depth = 0
        while root.val != val:
            my_list.append(root.val)
            if val > root.val:
                root = root.right
            else:
                root = root.left
            depth += 1
        return depth
    depth1 = get_depth(root,val1,list1)
    depth2 = get_depth(root,val2,list2)
    if not list1:
        return depth2
    if not list2:
        return depth1
    if depth1 > depth2:
        depth1,depth2,val1,val2,list1,list2 = depth2,depth1,val2,val1,list2,list1
    n = 0
    while n < len(list1):
        if list1[n] == list2[n]:
            n += 1
            continue
        else:
            break
    #tricky part
    lca = list1[n-1]
    if list2[n] == val1:
        return depth2-depth1
    else:
        return depth2 + depth1 - 2*n + 2
# test case:
class BSTree(object):

    def __init__(self):
        self.root = TreeNode(5)
        node = TreeNode(3)
        self.root.left = node
        node = TreeNode(6)
        self.root.right = node
        node = TreeNode(2)
        self.root.left.left = node
        node = TreeNode(4)
        self.root.left.right = node
        node = TreeNode(7)
        self.root.right.right = node
        node = TreeNode(1)
        self.root.left.left.left = node
        node = TreeNode(8)
        self.root.right.right.right = node

    def getBSTHead(self):
        return self.root
my_tree = BSTree()
#         5
#        / \
#       3   6
#      / \   \
#     2   4   7
#    /         \
#   1           8
print(get_distance(my_tree.getBSTHead(), 2,3)) #expect 1
print(get_distance(my_tree.getBSTHead(), 2,8)) #expect 5
print(get_distance(my_tree.getBSTHead(), 1,5)) #expect 3
print(get_distance(my_tree.getBSTHead(), 6,7)) #expect 1
print(get_distance(my_tree.getBSTHead(), 4,6)) #expect 3
        
            
        
