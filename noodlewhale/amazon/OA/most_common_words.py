#https://leetcode.com/problems/most-common-word/submissions/
#be careful of the usage of re.findall(r'\w+', paragraph.lower())
#time: O(number of words)
#spacce: O(number of words)
from collections import Counter
import heapq
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word_count = Counter(re.findall(r'\w+', paragraph.lower()))
        print(word_count)
        heap = []
        for key,value in word_count.items():
            heapq.heappush(heap,(-value,key))
        while heap:
            cur = heapq.heappop(heap)
            if cur[1] not in banned:
                return cur[1]
