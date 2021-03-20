#现在看来只需要prev_time...
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        prev_time = 0
        stack = []
        res = [0 for i in range(n)]
        for i in logs:
            task,t,ts = i.split(':')
            task = int(task)
            ts = int(ts)
            if t == "start":
                if stack:
                    res[stack[-1]] += ts-prev_time
                stack.append(task)
                prev_time = ts
            else:
                #this will make end time and start time align
                ts = ts + 1
                task = stack.pop()
                res[task] += ts-prev_time
                prev_time = ts
        return res
