#edge cases 有限状态机太恶心了
# 注意区分None 和 len(x) == 0 是不一样的
from collections import Counter
class Solution:
    def isNumber(self, s: str) -> bool:
        def is_only_digit(s):
            for i in s:
                if not ord('0') <= ord(i) <= ord('9'):
                    return False
            return True
        def is_decimal(s):
            if len(s) == 0:
                return False
            if s[0] in ['+','-']:
                s = s[1:]
            if len(s) == 0:
                return False
            s_c = Counter(s)
            if '.' not in s_c or s_c['.'] > 1:
                return False
            a , b = s.split('.')
            if len(a) == 0 and len(b) == 0:
                return False
            return is_only_digit(a) and is_only_digit(b)
        def is_integer(s):
            if len(s) == 0:
                return False
            if s[0] in ['+','-']:
                s = s[1:]
            if not s:
                return False
            return is_only_digit(s)
        def is_valid_e(s):
            s_c = Counter(s)
            num_e = 0 if 'e' not in s_c else s_c['e']
            num_E = 0 if 'E' not in s_c else s_c['E']
            return num_e + num_E == 1        
        if is_valid_e(s):
            if 'e' in s:
                a,b = s.split('e')
            else:
                a,b = s.split('E')
            return (is_decimal(a) or is_integer(a)) and is_integer(b)
        else:
            return is_decimal(s) or is_integer(s)
