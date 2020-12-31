#https://aonecode.com/amazon-online-assessment-shopping-patterns
#O(n**3)
#O(n**2)
def get_min(num_node,num_edge,product_from,product_to):
    pair_dict = {}
    trio_set = set()
    for i,j in zip(product_from,product_to):
        if i not in pair_dict:
            pair_dict[i] = [j]
        else:
            pair_dict[i].append(j)
        if j not in pair_dict:
            pair_dict[j] = [i]
        else:
            pair_dict[j].append(i)
    for i in pair_dict:
        if len(pair_dict[i]) >=2:
            for j in range(len(pair_dict[i])):
                k = 1
                while j+k < len(pair_dict[i]):
                    if pair_dict[i][j+k] in pair_dict[pair_dict[i][j]]:
                        trio_set.add(tuple(sorted([i,pair_dict[i][j],pair_dict[i][j+k]])))
                    k += 1
    res = float("inf")
    for trio in trio_set:
        a,b,c = trio[0], trio[1], trio[2]
        my_sum = 0
        external_set = set()
        for i in [a,b,c]:
            for j in pair_dict[i]:
                external_set.add(j)
        my_sum += len(external_set) - 3
        res = min(my_sum,res)
    return res

#test case:
print(get_min(num_node = 6, num_edge = 6, product_from = [1,2,2,3,4,5], product_to = [2,4,5,5,5,6]))
