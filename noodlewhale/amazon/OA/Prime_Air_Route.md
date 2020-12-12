```
#  O(n) solution usign two-pointer, duplicates issue is addressed.
# ugly solution though, need further optimize
def get_optimal_path(max_dist, forward_list, return_list):
    if not forward_list or not return_list:
        return 
    forward_list = sorted(forward_list, key = lambda x: x[1])
    return_list = sorted(return_list, key = lambda x: x[1])
    curr_max = float('-inf')
    left,right = 0, len(return_list)-1
    res = []
    while left < len(forward_list) and right >= 0 :
        index_left,index_right = forward_list[left][0], return_list[right][0]
        curr_sum = forward_list[left][1] + return_list[right][1]
        if curr_sum > max_dist:
            right -= 1
            continue
        if curr_sum < curr_max:
            left += 1
        elif curr_sum == curr_max:
            res.append([index_left,index_right])
            if left == len(forward_list)-1:
                right -= 1
            elif right == 0:
                left += 1
            else:
               #if both arrays have duplicates:
                if forward_list[left+1][1] == forward_list[left][1] and return_list[right-1][1] == return_list[right][1]:
                    left_start_index, left_start_value = forward_list[left][0], forward_list[left][1]
                    right_start_index, right_start_value = return_list[right][0], return_list[right][1]
                    left_list = [left]
                    right_list = [right]
                    left_end_index = left
                    right_end_index = right
                    for i in range(left+1, len(forward_list)):
                        if forward_list[i][1] == left_start_value:
                            left_list.append(i)
                        else:
                            left_end_index = i
                            break
                    for i in range(0, right)[::-1]:
                        if return_list[i][1] == right_start_value:
                            right_list.append(i)
                        else:
                            right_end_index = i
                            break
                    for i in left_list:
                        for j in right_list:
                            if not (i == left and j == right):
                                res.append([forward_list[i][0],return_list[j][0]])
                    if left_end_index == left:
                        left = len(forward_list)
                    else:
                        left = left_end_index
                    if right_end_index == right:
                        right = -1
                    else:
                        right = right_end_index
                elif forward_list[left+1][1] == forward_list[left][1]:
                    left +=1
                elif return_list[right-1][1] == return_list[right][1]:
                    right -=1
                else:
                    left += 1
        else:
            curr_max = curr_sum
            res = [[index_left,index_right]]
            if left == len(forward_list)-1:
                right -= 1
            elif right == 0:
                left += 1
            else:
                #if both arrays have duplicates:
                if forward_list[left+1][1] == forward_list[left][1] and return_list[right-1][1] == return_list[right][1]:
                    left_start_index, left_start_value = forward_list[left][0], forward_list[left][1]
                    right_start_index, right_start_value = return_list[right][0], return_list[right][1]
                    left_list = [left]
                    right_list = [right]
                    left_end_index = left
                    right_end_index = right
                    for i in range(left+1, len(forward_list)):
                        if forward_list[i][1] == left_start_value:
                            left_list.append(i)
                        else:
                            left_end_index = i
                            break
                    for i in range(0, right)[::-1]:
                        if return_list[i][1] == right_start_value:
                            right_list.append(i)
                        else:
                            right_end_index = i
                            break
                    for i in left_list:
                        for j in right_list:
                            if not (i == left and j == right):
                                res.append([forward_list[i][0],return_list[j][0]])
                    if left_end_index == left:
                        left = len(forward_list)
                    else:
                        left = left_end_index
                    if right_end_index == right:
                        right = -1
                    else:
                        right = right_end_index
                elif forward_list[left+1][1] == forward_list[left][1]:
                    left +=1
                elif return_list[right-1][1] == return_list[right][1]:
                    right -=1
                else:
                    left += 1
    return res






# test case:
print(get_optimal_path(11, [[1, 5], [2, 5]], [ [1, 5], [2, 5] ]))
print(get_optimal_path(10, [[1, 5], [2, 5]], [ [1, 5], [2, 5] ]))
print(get_optimal_path(20, [[1, 8], [2, 7], [3, 14]], [[1, 5], [2, 10], [3, 14]]))
print(get_optimal_path(20, [[1, 8], [2, 15], [3, 9]], [[1, 8], [2, 11], [3, 12]]))
print(get_optimal_path(7000, [[1, 2000], [2, 4000], [3, 6000]], [[1, 2000]]))
```
