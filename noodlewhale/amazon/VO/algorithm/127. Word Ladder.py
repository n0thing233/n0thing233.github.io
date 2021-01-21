#BFS
#not normal neighbors but smart neighbors,key is the shared pattern a*b
from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        pattern_dict = defaultdict(list)
        for i in set([beginWord,endWord] + wordList):
            for j in range(len(i)):
                pattern_dict[i[:j]+'*'+i[(j+1):]].append(i)
        queue = deque()
        queue.append((beginWord,1))
        res = float('inf')
        visited = set()
        while queue:
            i,steps = queue.popleft()
            if i == endWord:
                return steps
            for j in range(len(i)):
                for k in pattern_dict.pop(i[:j]+'*'+i[(j+1):],[]):
                    if k == i or k in visited:
                        continue
                    queue.append((k,steps+1))
        return 0 if res == float('inf') else res
