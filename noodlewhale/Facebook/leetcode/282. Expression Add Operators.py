#backtracking brute-force。。。
#关键点： 1.把不插符号转化为加隔板问题 (speical case backtracking)
#        2. edge case 055 invalid number 
#        3.记录last_added,可以处理*的问题
#        4.不可以直接从index == 1开始。因为index = 0的 char 还可以和后边的char组合成一个数字
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if not num:
            return []
        self.res = []
        def helper(num,target,path,index,curr,last_added):
            if index == len(num):
                if curr == target:
                    self.res.append(path[:])
            for i in range(index,len(num)):
                if num[index] == '0' and i!=index:
                    break
                tmp = int(num[index:(i+1)])
                #坑，这个坑是你把不插符号转化为隔板问题留下的。对于index = 0无论i 是谁，都不能加。因为第一个index之前不能加符号。
                if index == 0:
                    helper(num,target,num[index:(i+1)],i+1,tmp,tmp)
                    continue
                helper(num,target,path+"+"+num[index:(i+1)],i+1,curr+tmp,tmp)
                helper(num,target,path+"-"+num[index:(i+1)],i+1,curr-tmp,-tmp)
                helper(num,target,path+"*"+num[index:(i+1)],i+1,curr-last_added+last_added*tmp,last_added*tmp)
            return
        helper(num,target,'',0,0,0)
        return self.res
