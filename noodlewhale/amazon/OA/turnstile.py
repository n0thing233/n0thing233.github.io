#https://aonecode.com/amazon-online-assessment-turnstile
#time:O(max time)
#space: O(num)
from collections import deque
def get_time(num,arrTime,direction):
    res = []
    if not num or num <= 0 :
        return res
    res = [-1]*num
    #at a certain timestamp, if no one arrive and no one queued, then do nothing
    #decide who should go through
    # type1: ppl arrived
    # type2: ppl queued.
    # put ppl arrived in the queue and pop from queue.
    # have a queue for each direction ,determine which queue to pop
    queue_enter = deque()
    queue_exit = deque()
    arr_dict = {}
    for i in range(len(arrTime)):
        if arrTime[i] not in arr_dict:
            arr_dict[arrTime[i]]  = [i]
        else:
            arr_dict[arrTime[i]].append(i)
    #print(arr_dict)
    time = counter = 0 
    prev_direction = 1
    while counter < num:
        if time in arr_dict:
            curr_indices = sorted(arr_dict[time]) 
            for index in curr_indices:
                if direction[index] == 1:
                    queue_exit.append(index)
                else:
                    queue_enter.append(index)
        if prev_direction == 1:
            if queue_exit:
                index = queue_exit.popleft()
                res[index] = time
                counter += 1
                prev_direction = 1
            elif queue_enter:
                index = queue_enter.popleft()
                res[index] = time
                counter += 1
                prev_direction = 0
            else:
                prev_direction = 1
        else:
            if queue_enter:
                index = queue_enter.popleft()
                res[index] = time
                counter += 1
                prev_direction = 0
            elif queue_exit:
                index = queue_exit.popleft()
                res[index] = time
                counter += 1
                prev_direction = 1
            else:
                prev_direction = 1
        #print("time is " + str(time))
        #print("queue enter is" + str(queue_enter))
        #print("exit queue is" + str(queue_exit))
        #print(res)
        time += 1
    return res
#building test cases here:
print(get_time(4,[0,0,1,5],[0,1,1,0])) #expect [2,0,1,5]
print(get_time(5,[1,1,1,3,3],[0, 1, 0, 1, 0])) #expect[0, 2, 1, 4, 3]
print(get_time(2,[1,1],[1,0]))#expect [1,2]
                
            
