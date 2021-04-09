#很难，segment tree
#bug_count :12 bugs for the first time segment tree implementation, not too bad!!!!!!!!!
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        #by theory
        self.tree = [0 for i in range(len(nums)*4)]
        self.tree_length = 0
        self._build_tree(nums, 0,0,len(nums)-1)
    def _build_tree(self,nums,tree_index,left,right):
        if left == right:
            self.tree[tree_index] = nums[left]
            return
        mid = left + (right-left)//2
        self._build_tree(nums,tree_index*2+1,left,mid)
        self._build_tree(nums,tree_index*2+2,mid+1,right)
        self.tree[tree_index] = self.tree[tree_index*2+1] + self.tree[tree_index*2+2]
        return
    def _update_tree(self,tree_index,left,right,num_index,val):
        if left == right:
            self.tree[tree_index] = val
            return
        mid = left + (right-left)//2
        if mid < num_index:
            self._update_tree(tree_index*2+2,mid+1,right,num_index,val)
        else:
            self._update_tree(tree_index*2+1,left,mid,num_index,val)
        self.tree[tree_index] = self.tree[tree_index*2+1] + self.tree[tree_index*2+2]
        return
    def update(self, index: int, val: int) -> None:
        return self._update_tree(0,0,len(self.nums)-1,index,val)
    
    def _sum_range(self,tree_index,left,right,lo,hi):
        if lo > right or hi < left:
            return 0
        if lo <= left and hi >= right:
            return self.tree[tree_index]
        mid = left + (right-left)//2
        if mid < lo:
            return self._sum_range(tree_index*2+2,mid+1,right,lo,hi)
        elif mid > hi:
            return self._sum_range(tree_index*2+1,left,mid,lo,hi)
        left_sum = self._sum_range(tree_index*2+1,left,mid,lo,mid)
        right_sum = self._sum_range(tree_index*2+2,mid+1,right,mid+1,hi)
        return left_sum + right_sum
    def sumRange(self, left: int, right: int) -> int:
        return self._sum_range(0,0,len(self.nums)-1,left,right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
