class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        res = []
        for case in [S, T]:
            temp = []
            for c in case:
                if c == '#':
                    if len(temp) > 0:
                        temp.pop()
                else:
                    temp.append(c)
            res.append(temp)
        return res[0] == res[1]



S = "y#fo##f"
T = "y#f#o##f"
print(Solution().backspaceCompare(S, T))
