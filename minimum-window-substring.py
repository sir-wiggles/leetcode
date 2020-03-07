from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need = Counter(t)
        missing = len(t)
        i = 0
        I, J = 0, 0
        for j, c in enumerate(s, start=1):
            missing -= 1 if need[c] > 0 else 0
            need[c] -= 1
            if missing == 0:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i < J - I:
                    I, J = i, j
        return s[I:J]


#  A: 0
#  B: 0
#  C: 0
# 
#  missing = 0

# 0,6

#             |  |
s = "ADOBECODEBANC"
#    0123456789012
#              111
t = "ABC"
print(Solution().minWindow(s, t))
