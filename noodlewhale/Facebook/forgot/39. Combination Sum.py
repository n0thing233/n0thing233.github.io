#dfs brute-force, no you cant you will have duplciate. you need to sort and onyl traverse elements from #current index
#10:04 10:15
#time:O(N^(T/M))
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        n = len(candidates)
        res = []
        def helper(index,cur_sum,path,target):
            if cur_sum == target:
                res.append(path[:])
                return
            if cur_sum > target:
                return
            for i in range(index,n):
                path.append(candidates[i])
                cur_sum += candidates[i]
                helper(i,cur_sum,path,target)
                cur_sum -= candidates[i]
                path.pop()
            return
        helper(0,0,[],target)
        return res
