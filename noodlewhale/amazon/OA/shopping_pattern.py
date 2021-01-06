#https://aonecode.com/amazon-online-assessment-shopping-patterns
#O(V+E)
#O(V+E)
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
    print(trio_set)
    for trio in trio_set:
        a,b,c = trio[0], trio[1], trio[2]
        my_sum = 0
        for i in [a,b,c]:
            my_sum += len(pair_dict[i])-2
        res = min(my_sum,res)
    return res
