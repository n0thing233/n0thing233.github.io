#dp[i]定义不是到第i个的最小cost,而是从i能走到最后的最小cost
#所以你现在脑子里应该有三种dp方式了。从前到后，从后到前，以及从前到后的二维


from functools import lru_cache
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        @lru_cache
        def helper(i):
            if i >= n:
                return 0
            elif i == n-1:
                return min(costs)
            else:
                res = float('inf')
                for idx, duration in enumerate([1,7,30]):
                    index = i+1
                    while index < n and days[index] < days[i]+duration:
                        index += 1
                    res = min(res,helper(index) + costs[idx])
                return res
        return helper(0)
