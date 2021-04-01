#审题不仔细。。必须连续last k ,不能跳。。
#最重要的技巧就是reverse all,不然就要maintain waitlist 很烦。
#trie
class TrieNode():
    def __init__(self,value = None):
        self.val = None
        self.children = {}
class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for i in words:
            self._add_to_root(i[::-1])
        self.window = ''
        self.window_size = max([len(i) for i in words]) 
    def _add_to_root(self,word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.val = word
        

    def query(self, letter: str) -> bool:
        self.window = letter + self.window
        self.window = self.window[:self.window_size]
        node = self.root
        for i in self.window:
            if i not in node.children:
                return False
            node = node.children[i]
            if node.val:
                return True
        return False
