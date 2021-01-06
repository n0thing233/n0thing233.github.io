#一点都不简单啊
#time: O(n)
#space: O(len(s))
def get_all(s,startIndices,endIndices):
    num_of_compartment = []
    count = 0
    index_dict = {}
    for i in range(len(s)):
        if s[i] == '|':
            index_dict[count] = i
            count += 1
        num_of_compartment.append(count)
    res = []
    for i in range(len(startIndices)):
        start, end = max(0,startIndices[i]-1), min(len(s)-1,endIndices[i]-1)
        num_start, num_end = num_of_compartment[start], num_of_compartment[end]
        #edge case if num_start = num_end:
        if num_start >= num_end:
            res.append(0)
            continue
        if s[start] == "*" and s[end] == "*":
            res.append(index_dict[num_end-1] - index_dict[num_start] - (num_end-1 -num_start))
        elif s[end] == "*" :
            res.append(index_dict[num_end-1] - index_dict[num_start-1] - (num_end -num_start))
        elif s[start] == "*":
            res.append(index_dict[num_end-1] - index_dict[num_start] - (num_end-1 -num_start))
        else:
            res.append(index_dict[num_end-1] - index_dict[num_start-1] - (num_end -num_start))
    return res

#test case:
s1 = "|**|*|*"
print("Items in " + s1 + " : " + str(get_all(s1, [1, 1], [5, 6]))) #Output is [2, 3]

s2 = "*|*"
print("Items in " + s2 + " : " + str(get_all(s2, [0], [3])))  #Output is [0]

s3 = "****|*|";
print("Items in " + s3 + " : " + str(get_all(s3, [0, 4, 2], [3, 7, 7]))) #Output is [0, 1, 1]
