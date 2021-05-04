#9:45 10:14
#也算半小时把不需要变成tree的做法做出来了，最关键的就是要有一个num_dict
class Solution:
    def pathSum(self, nums: List[int]) -> int:
        self.res = 0
        num_dict = {}
        for i in nums:
            num_dict[i//10] = i%10
        def helper(node_prefix,carry):
            carry += num_dict[node_prefix]
            level = node_prefix//10
            index = node_prefix%10
            left_prefix = (level+1)*10+index*2-1
            right_prefix = (level+1)*10+index*2
            if left_prefix not in num_dict and right_prefix not in num_dict:
                self.res += carry
                return
            if left_prefix in num_dict:
                helper(left_prefix,carry)
            if right_prefix in num_dict:
                helper(right_prefix,carry)
        helper(nums[0]//10,0)
        return self.res
