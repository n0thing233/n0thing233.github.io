#https://algo.monster/problems/earliest_time_to_complete_deliveries
def get_earliest_time(numOfBuildings,buildingOpenTime,offloadTime):
    n = numOfBuildings
    open_time = buildingOpenTime
    offloadtime = offloadTime
    res = float('-inf')
    open_time = sorted(open_time)
    offloadtime = sorted(offloadtime)
    for i in open_time:
        count = 0
        while count <= 3:
            curr = offloadtime.pop()
            res = max(res,curr+i)
            count += 1
    return res
#test cases:
print(get_earliest_time(2,[8,10],[2,2,3,1,8,7,4,5])) #expect 16
