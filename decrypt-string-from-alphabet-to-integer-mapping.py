from string import ascii_lowercase
from collections import defaultdict

class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s)-1
        res = []
        while i >= 0:
            if s[i] == '#':
                res.append(ascii_lowercase[int(s[i-2:i])-1])
                i -= 3
            else:
                res.append(ascii_lowercase[int(s[i])-1])
                i -= 1
        return ''.join(res[::-1])



s = "10#11#12"
#  s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
print(Solution().freqAlphabets(s))
