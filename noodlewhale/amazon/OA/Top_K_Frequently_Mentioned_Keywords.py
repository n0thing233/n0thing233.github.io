#https://leetcode.com/discuss/interview-question/580505/amazon-sde-oa-question-2020-amazon-oa-2020-top-k-frequently-mentioned-keywords
#O(n)
#O(n)
#heapq with custom implementation of __lt__
from collections import defaultdict
import heapq
class keyword_priority(object):
    def __init__(self,num = None,string = None):
        self.num = num
        self.string = string
    def __lt__(self,other):
        if self.num != other.num:
            return self.num < other.num
        else:
            return self.string > other.string
def find_top_k(reviews,keywords,k):
    #build dictionary
    word_cnt = defaultdict(int)
    for i in keywords:
        for j in reviews:
            if i in j:
                word_cnt[i] += 1
    #print(word_cnt)
    min_heap = []
    for i in word_cnt:
        heapq.heappush(min_heap,keyword_priority(num = word_cnt[i],string = i))
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    #print(min_heap)
    return [i.string for i in min_heap]

reviews = ["I wish my Kindle had even more storage.",
                "I wish the battery life on my Kindle lasted 2 years.",
                "I read in the bath and would enjoy a waterproof Kindle.",
                "waterproof and increased battery are my top two requests.",
                "I want to take my Kindle intor the shower. Waterproof please waterproof!",
                "I would be neat if my Kindle would hover on my desk when not in use.", 
                "How cool would it be if my Kindle charged in the sun via solar power."]
keywords = ["storage", "battery", "hover", "alexa", "waterproof", "solar"]
k = 3
print (find_top_k(reviews, keywords, k))
