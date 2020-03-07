class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:

        S = S.upper().replace('-', '')[::-1]

        res = []
        for i, c in enumerate(S, start=1):
            res.append(c)
            if i % K == 0 and i != len(S):
                res.append('-')

        return ''.join(res[::-1])



S = "5F3Z-2e-9-w"
K = 4
print(Solution().licenseKeyFormatting(S, K))

S = "2-5g-3-J"
K = 2
print(Solution().licenseKeyFormatting(S, K))

S = "--a------a-a-a-a----"
K = 2
print(Solution().licenseKeyFormatting(S, K))

