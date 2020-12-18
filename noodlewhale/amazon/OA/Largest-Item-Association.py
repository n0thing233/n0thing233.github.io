#https://leetcode.com/discuss/interview-question/782606/
#return the largest connected component
from collections import deque
def largest_item_association(item_association):
    if not item_association:
        return
    neighbors = {}
    for i in item_association:
        if i[0] not in neighbors:
            neighbors[i[0]] = [i[1]]
        else:
            neighbors[i[0]].append(i[1])
        if i[1] not in neighbors:
            neighbors[i[1]] = [i[0]]
        else:
            neighbors[i[1]].append(i[0])
    visited = {}
    for i in neighbors:
        visited[i] = False
    max_component = []
    def dfs(neighbors, item, visited):
        if visited[item]:
            return []
        res = []
        stack = deque()
        stack.append(item)
        while stack:
            curr = stack.pop()
            if visited[curr]:
                continue
            res.append(curr)
            for item in neighbors[curr]:
                #this is optional
                if visited[curr]:
                    continue
                stack.append(item)
            visited[curr] = True
        return res
    for item in visited:
        if visited[item]:
            continue
        curr_list = dfs(neighbors,item,visited)
        if len(curr_list) > len(max_component):
            max_component = curr_list
    return max_component

print(largest_item_association([['item1', 'item2'], ['item3', 'item4'], ['item4', 'item5'], ['item5', 'item6']]))
print(largest_item_association([['item6', 'item7'], ['item3', 'item4'], ['item4', 'item5'], ['item7', 'item8']]))
print(largest_item_association([['item1', 'item2'], ['item4', 'item5'], ['item3', 'item4'], ["item1","item4"]]))
