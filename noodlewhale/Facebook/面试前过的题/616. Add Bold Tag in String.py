class TrieNode:
    def __init__(self):
        self.length = None
        self.children = {}
class Solution:
    def __init__(self):
        self.root = TrieNode()
    def add_to_root(self,s):
        node = self.root
        for i in s:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.length = len(s)
    def get_max_match(self,s):
        node = self.root
        max_matched = 0
        for i in s:
            if i not in node.children:
                break
            node = node.children[i]
            if node.length is not None:
                max_matched = node.length
        return max_matched
    def add_bold(self,s,is_bold):
        res = ''
        if is_bold[0]:
            res = '<b>' + res
        for i in range(len(s)-1):
            res += s[i]
            if is_bold[i] == False and is_bold[i+1] == True:
                res += '<b>'
            elif is_bold[i] == True and is_bold[i+1] == False:
                res += '</b>'
        res += s[len(s)-1]
        if is_bold[-1]:
            res += '</b>'
        return res
        
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        for i in dict:
            self.add_to_root(i)
        is_bold = [False for i in range(len(s))]
        for i in range(len(s)):
            max_matched = self.get_max_match(s[i:])
            for j in range(i,i+max_matched):
                is_bold[j] = True
        return self.add_bold(s,is_bold)
