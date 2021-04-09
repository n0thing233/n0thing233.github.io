#一开始以为理解了。。大概就是dfs到不能走了，那这个node一定是end.
#要保证可以valid走完所有edgezhi有两种情况：
#1.起点就是终点，这样的话，每个点都可以作为起点，切每个点的indegree和outdegree都应该相等
#2.起点不是终点，这样的话，起点的outdegree - indegree = 1 终点的indegree - outdegree = 1
#总结的话，一个图可以每个edge走完切仅走完一次的充分必要条件是，out-degree- indegree = 1 的点的个数 <= 1 indegree - outdgree = 1 的点的个数 <= 1.且其他点的indegree = out degree
#这道题已经告诉你可以走完，且已经告诉你起点是jfk,所以可以直接开始dfs.从后到前build result
#先走lexical 较小的点，所以backtrack往里加到res会最后加娇小的点
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        t_d = {}
        for ticket in sorted(tickets)[::-1]:
            d = ticket[0]
            a = ticket[1]
            if d not in t_d:
                t_d[d] = []
            t_d[d].append(a)
        res = []
        def dfs(a):
            while a in t_d and t_d[a]:
                dfs(t_d[a].pop())
            res.append(a)
        dfs('JFK')
        return res[::-1]
