# O(n)
#O(n)
#https://aonecode.com/amazon-online-assessment-five-star-sellers
import heapq
def get_min_step(ratings,threshold):
    n = len(ratings)
    sum_goal = threshold*n*0.01
    sum_curr = 0
    res = 0
    product_tuples = []
    def get_gain(rating):
        return -(float(rating[0]+1)/float(rating[1]+1)-float(rating[0])/float(rating[1]))
    for rating in ratings:
        sum_curr += float(rating[0])/float(rating[1])
        product_tuples.append((get_gain(rating),rating))
    if sum_curr >= sum_goal:
        return res
    heapq.heapify(product_tuples)
    counter = 0
    while sum_curr < sum_goal:
        #print(product_tuples)
        gain, rating = heapq.heappop(product_tuples)
        sum_curr -= gain
        counter += 1
        rating[0] += 1
        rating[1] += 1
        heapq.heappush(product_tuples, (get_gain(rating),rating))
    return counter

#test cases:
print(get_min_step([[4,4], [1,2], [3, 6]],77)) #expect 3
print(get_min_step([[9,10]],91)) #expect 2
print(get_min_step([[1,3],[1,4]],60)) #expect 6
