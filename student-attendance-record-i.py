from collections import defaultdict

class Solution:
    def checkRecord(self, s: str) -> bool:

        m = defaultdict(list)
        for i, c in enumerate(s, start=1):
            if c == 'L' and s[i-1:i+2].count('L') > 2:
                return False
            m[c] += 1

        if m['A'] > 1:
            return False
        return True


test = 'LPLLPALLPLL'
print(Solution().checkRecord(test))
