#和word ladder思路一样，但要求以下几点优化：
#1. i*（i+1）    2. visited and local_visited. level_length
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        res = []
        q = collections.deque()
        q.append([beginWord])
        visited = set()
        visited.add(beginWord)
        
        word_dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                word_dict[word[:i]+"*"+word[(i+1):]].append(word)
        while q:
            level_length = len(q)
            to_be_visited = set()
            for _ in range(level_length):
                path = q.popleft()
                if path[-1] == endWord:
                    res.append(path[:])        
                for i in range(len(path[-1])):
                    for x in word_dict[path[-1][:i]+"*"+path[-1][(i+1):]]:
                        if x not in visited:
                            to_be_visited.add(x)
                            q.append(path+[x])
            visited = visited.union(to_be_visited)
            if res:
                return res
