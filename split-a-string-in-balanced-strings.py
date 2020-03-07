class Solution:
    def balancedStringSplit(self, s: str) -> int:
        bal, count = 0, 0
        for c in s:
            if c == 'R':
                bal += 1
            else:
                bal -= 1

            if bal == 0:
                count += 1
        return count



i = [
"RLRRLLRLRL",
"RLLLLRRRLR",
"LLLLRRRR"  ,
"RLRRRLLRLL",
]
for case in i:
    print(Solution().balancedStringSplit(case))
