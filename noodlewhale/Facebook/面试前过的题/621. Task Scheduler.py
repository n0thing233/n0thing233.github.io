#关键在于availabe tasks里的task是可以随便放到slot里的，因为他的freq不是最大的，所以一个partition放一个，是放不完一圈的
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        t_c = Counter(tasks)
        max_freq = 0
        max_freq_tasks = []
        for i in t_c:
            if t_c[i] > max_freq:
                max_freq = t_c[i]
                max_freq_tasks = [i]
            elif t_c[i] == max_freq:
                max_freq_tasks.append(i)
        
        number_of_slots = (n - len(max_freq_tasks)+1)*(max_freq-1)
        remaining_tasks = len(tasks) - max_freq*len(max_freq_tasks)
        
        if number_of_slots <=0:
            return len(tasks)
        if number_of_slots < remaining_tasks:
            return len(tasks)
        slots_needed = number_of_slots - remaining_tasks
        return len(tasks) + slots_needed
