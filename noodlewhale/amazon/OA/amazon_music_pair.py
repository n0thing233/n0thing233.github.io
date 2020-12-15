#https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/submissions/
#O(n)??
# 做个简单题压压惊，只考虑余数就可以。。。。
from collections import Counter
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time = [number%60 for number in time]
        time_counter = Counter(time)
        res = 0
        if time_counter[0] >= 1:
            res += time_counter[0]*(time_counter[0]-1)//2
        if time_counter[30] >= 1:
            res += time_counter[30]*(time_counter[30]-1)//2
        for i in range(1,30):
            res += time_counter[i]*time_counter[60-i]
        return res
