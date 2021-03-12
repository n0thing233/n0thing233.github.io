#n = 27
#request_time = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,11,11,11,11]
#rule: same second cannot exceed 3
# 10 secs cannot exceed 20
# 60 secscannot exceed 60
#intuation: prefix_sum
#return number throttled requests:
from collections import Counter
def get_throttled(n,request_time):
    r_c = Counter(request_time)
    prefix = [0 for i in range(max(request_time)+1)]
    for i in range(1,len(prefix)):
        to_add = 0 if i not in r_c else r_c[i]
        prefix[i] = prefix[i-1] + to_add
    print(r_c)
    print(prefix)
    res = 0
    for i in r_c:
        total = r_c[i]
        throttle_1 = max(0,total - 3)
        if i-10 < 0:
            throttle_2 = max(0, prefix[i] - 20)
        else:
            throttle_2 = max(0, min(total,prefix[i]-prefix[i-10] - 20))
        if i-60 < 0:
            throttle_3 = max(0, prefix[i] - 60)
        else:
            throttle_3 = max(0, min(total,prefix[i]-prefix[i-60] - 60))
        
        res += max(throttle_1,throttle_2,throttle_3)
        print("current key is " + str(i))
        print("curent sum is " + str(res))
    return res
print(get_throttled(27,[1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,11,11,11,11]))
