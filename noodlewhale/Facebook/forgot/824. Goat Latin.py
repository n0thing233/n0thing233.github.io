#忘记了大小写！！！！！！AEIOU
class Solution:
    def toGoatLatin(self, S: str) -> str:
        S = S.split()
        def process(w,idx):
            if w[0] in ['a','e','i','o','u','A','E','I','O','U']:
                w = w + 'ma'
            else:
                w = w[1:]+w[0] + 'ma'
            w = w + 'a'*(idx+1)
            return w
        for idx,word in enumerate(S):
            S[idx]  = process(word,idx)
        return ' '.join(S)
