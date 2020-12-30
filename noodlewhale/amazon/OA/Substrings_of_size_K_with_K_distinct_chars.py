#https://leetcode.com/discuss/interview-question/370112/
#time:O(n)
#space:O(1)
from collections import defaultdict
def get_substring(string,k):
    if not string:
        return
    n = len(string)
    if n < k:
        return
    res = []
    char_count = defaultdict(int)
    for i in range(0,k):
        char_count[string[i]] += 1
    if len(char_count) == k:
        res.append(string[:k])
    for i in range(k, n):
        char_count[string[i]] += 1
        char_count[string[i-k]] -= 1
        if char_count[string[i-k]] == 0:
            del char_count[string[i-k]]
        if len(char_count) == k:
            res.append(string[i-k+1:i+1])
    return res
#test cases:
print(get_substring("abcabc",3))#expect : ["abc", "bca", "cab"]
print(get_substring("abacab",3))#expect : ['bac', 'cab']
print(get_substring("awaglknagawunagwkwagl",4))#expect : ['wagl', 'aglk', 'glkn', 'lkna', 'knag', 'gawu', 'awun', 'wuna', 'unag', 'nagw', 'agwk', 'kwag', 'wagl']
        
