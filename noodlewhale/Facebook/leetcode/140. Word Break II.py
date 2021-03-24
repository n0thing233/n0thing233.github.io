#top-down dp with memo
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s:
            return []
        if not wordDict:
            return []
        memo = {}
        def helper(s):
            if s in memo:
                return memo[s]
            if s == '':
                return [[]]
            res = []
            for word in wordDict:
                if s.startswith(word):
                    for i in helper(s[len(word):]):
                        res.append([word]+i)
            memo[s] = res
            return res
        return [' '.join(i) for i in helper(s)]
