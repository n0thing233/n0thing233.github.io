#intuation,graph trie
#from the words build DAG
#topological sort DAG, if cycle return "", else return sort.
#time:O(V+E)
#space:O(V+E)
from collections import defaultdict
from collections import deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        n = len(words)
        neighbors = defaultdict(list)
        def get_order_from_word_pair(w1,w2,neighbors):
            l1,l2 = len(w1),len(w2)
            index = 0
            while index < l1 and index < l2:
                if w1[index] == w2[index]:
                    index += 1
                    continue
                else:
                    neighbors[w1[index]].append(w2[index])
                    return True
            #edge case.
            return False if l1 > l2 else True         
        for i in range(n-1):
            for j in range(i+1,n):
                if not get_order_from_word_pair(words[i],words[i+1],neighbors):
                    return ""        
        #bfs topological sort with indegree
        indegree = {}
        #edge case some letters in the graph are not in neighbors dict, it is always best practice to insert all nodes into indegree frist and then update count for each node.
        #put all characters into indegree:
        for i in words:
            for j in i:
                if j not in indegree:
                    indegree[j] = 0
        for i,j in neighbors.items():
            for k in j:
                indegree[k] += 1
        queue = deque()
        for i in indegree:
            if indegree[i] == 0:
                queue.append(i)
        res = []
        while queue:
            curr = queue.pop()
            for i in neighbors[curr]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
            res.append(curr)
        return "".join(res) if len(res) == len(indegree) else ""
