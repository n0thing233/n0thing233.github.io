#https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/submissions/
#小镇做题家的极限？
#这题就理解到top-down dp 遍历就可以了。bottom-up 2 dimension 以及后来的1 dimension 需要花大量时间
#或者建立大量dp神经元来理解，世纪面试中用不到先放弃。。这题就记住top-down的状态转换。
#求dfs(0,d),其中0代表从jobDifficulty的第0个index开始，一直到结束要安排d天完成的minimum cost.
#并且了解python 中lru_cache的用法。

# 记住time: O(n*n*d) recursive time compliexity is always tricky.
# space:O(nd)
import functools
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n:
            return -1
        @functools.lru_cache(None)
        def dfs(index,d):
            if d == 1:
                return max(jobDifficulty[index:])
            max_cur , min_cost = float('-inf'), float('inf')
            for j in range(index, n-d+1):
                max_cur = max(max_cur,jobDifficulty[j])
                min_cost = min(min_cost,max_cur + dfs(j+1, d-1))
            return min_cost
        return dfs(0,d)
