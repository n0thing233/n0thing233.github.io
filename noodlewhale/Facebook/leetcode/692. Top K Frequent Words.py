#two approach
#quickselect+sorting
#O(n)+klogk
#2:00
#又写了一个小时。。
#bug1: 找最大不能用n-k-1会变成-1.。。
#bug2: alphbetical order和最大最小是两个方向
import random
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        w_c = Counter(words)
        key_array = [i for i in w_c]
        n = len(key_array)
        def partition(key_array,left,right):
            picked = random.randint(left,right)
            key_array[left],key_array[picked] = key_array[picked],key_array[left]
            index = left + 1
            for i in range(left+1,right+1):
                if w_c[key_array[i]] < w_c[key_array[left]]:
                    key_array[i],key_array[index] = key_array[index],key_array[i]
                    index += 1
                elif w_c[key_array[i]] == w_c[key_array[left]] and key_array[i] > key_array[left]:
                    key_array[i],key_array[index] = key_array[index],key_array[i]
                    index += 1
            key_array[left],key_array[index-1] = key_array[index-1],key_array[left]
            return index-1
        def quickselect(key_array,left,right,k):
            pivot = partition(key_array,left,right)
            if pivot == k:
                return key_array[pivot:]
            elif pivot > k:
                return quickselect(key_array,left,pivot-1,k)
            else:
                return quickselect(key_array,pivot+1,right,k)
        k_keys = quickselect(key_array,0,n-1,n-k)
        k = [[w_c[i],i] for i in k_keys]
        return [i[1] for i in sorted(k,key = lambda x : (-x[0],x[1]))]
