#https://aonecode.com/amazon-online-assessment-items-in-containers
#time: O(len(s)*len(startIndices))
#space: O(len(s))
def get_all(s,startIndices,endIndices):
    res = []
    def get_num_of_items(s):
        start_index = float('inf')
        end_index = float('-inf')
        for i in range(len(s)):
            if s[i] == '|':
                start_index = i
                break
        for i in range(len(s))[::-1]:
            if s[i] == '|':
                end_index = i
                break
        if start_index >= end_index:
            
            return 0
        else:
            counter = 0
            for i in range(start_index, end_index):
                if s[i] == '*':
                    counter +=1
            return counter
    for i in range(len(startIndices)):
        start = max(0, startIndices[i]-1)
        end = min(len(s)-1, endIndices[i]-1)
        res.append(get_num_of_items(s[start:(end+1)]))
    return res

#test case:
s1 = "|**|*|*"
print("Items in " + s1 + " : " + str(get_all(s1, [1, 1], [5, 6]))) #Output is [2, 3]

s2 = "*|*"
print("Items in " + s2 + " : " + str(get_all(s2, [0], [3])))  #Output is [0]

s3 = "****|*|";
print("Items in " + s3 + " : " + str(get_all(s3, [0, 4, 2], [3, 7, 7]))) #Output is [0, 1, 1]
