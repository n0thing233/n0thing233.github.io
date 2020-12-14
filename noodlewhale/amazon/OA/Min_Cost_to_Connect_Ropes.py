
import heapq
def get_minimum_cost(ropes):
    res = 0
    heapq.heapify(ropes)
    while (len(ropes) >=2):
        rope1 = heapq.heappop(ropes)
        rope2 = heapq.heappop(ropes)
        rope_sum = rope1 + rope2
        res += rope_sum
        heapq.heappush(ropes, rope_sum)
    return res
    
    

print(get_minimum_cost([8, 4, 6, 12]))   # 58
print(get_minimum_cost([20, 4, 8, 2]))    # 54
print(get_minimum_cost([1, 2, 5, 10, 35, 89]))     #224
print(get_minimum_cost([2, 2, 3, 3]))    #20

