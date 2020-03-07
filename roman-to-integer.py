from collections import deque

class Solution:
    def romanToInt(self, s: str) -> int:
        m = dict([
            ('I', 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000),
            (' ', 0)
        ])
        total = 0
        digits = deque(s + ' ')
        while digits:
            D = digits.popleft()
            if m[D] == 0:
                break
            if m[D] < m[digits[0]]:
                total = total + m[digits[0]] - m[D]
                digits.popleft()
            else: 
                total += m[D]
        return total

            

cases = [
    "III",
    "IV",
    "IX",
    "LVIII",
    "MCMXCIV"
]

for case in cases:
    print(Solution().romanToInt(case))
