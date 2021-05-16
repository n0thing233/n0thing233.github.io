#细节拉满题。这题需要一直做。。。
# start: 1.stack empty 2. stack have start if last_end if not last_end
# end : 1. last_end is not None, 2. last_end is None.
# bug :  change str to int....
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        def parse(s):
            x = s.split(':')
            return int(x[0]),x[1],int(x[2])       
        res = [0 for i in range(n)]
        stack = []
        last_ended = None
        for log in logs:
            job_id,job_type,ts = parse(log)
            if job_type == 'start':              
                if stack:
                    if last_end:
                        stack[-1][2] += ts - last_end - 1
                    else:
                        stack[-1][2] = ts - stack[-1][1]                    
                stack.append([job_id,ts,None])
                last_end = None
            else:
                if not last_end:
                    res[stack[-1][0]] += (ts - stack[-1][1]+1)
                else:
                    res[stack[-1][0]] += (stack[-1][2] + ts-last_end)
                stack.pop()
                last_end = ts
        return res
