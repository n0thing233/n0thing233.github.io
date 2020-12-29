#time:O(n)
#space:O(1)
#https://aonecode.com/amazon-online-assessment-utilization-checks
import math
def finalInstances(instances, averageUtil):
    """
    :type instances: int
    :type averageUtil: List[int]
    :rtype: int
    """
    index = 0
    n = len(averageUtil)
    while index < n:
        curr = averageUtil[index]
        action = False
        if curr < 25:
            if instances > 1:
                instances = math.ceil(instances/2)
                action = True
        elif curr > 60:
            if 2*instances <= 2*(10**8):
                instances *= 2
                action = True
        if action:
            index += 10
        else:
            index += 1
    return instances

#test case:
print(finalInstances(1, [5, 10, 80])) #expect 2
print(finalInstances(5, [30, 5, 4, 8, 19, 89])) #expect 3
