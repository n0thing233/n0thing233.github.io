#先处理最高的最后处理最低的，因为只有比你高的才能影响你的相对位置。
#greedy 看天赋啊朋友。。。
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people,key = lambda x : (-x[0],x[1]))
        res = []
        for i in people:
            res.insert(i[1],i)
        return res
