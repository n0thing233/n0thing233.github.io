#https://aonecode.com/amazon-online-assessment-lru
from collections import deque
def lruCacheMisses(num: int, pages: list, maxCacheSize: int) -> int:
    cache = deque()
    res = 0
    for i in pages:
        if i not in cache:
            res += 1
            cache.append(i) 
            if len(cache) == maxCacheSize+1:
                cache.popleft()
        else:
            cache.remove(i) 
            cache.append(i) 
    return res
            
