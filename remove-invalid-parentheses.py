from typing import List
from functools import lru_cache

class Solution:
    def removeInvalidParentheses(self, S: str) -> List[str]:

        ivl = ivr = 0
        l = r = 0
        for c in S:
            if c == "(":
                ivl += 1
                l += 1
            elif c == ")":
                r += 1
                if ivl == 0:
                    ivr += 1
                else:
                    ivl -= 1

        pairs = l - ivl
        valid = set()

        @lru_cache(None)
        def helper(i, s, l, r, o):

            if i == len(S) and l == r == pairs and o == 0:
                valid.add(s)

            if i == len(S):
                return 

            ll, rr = 0, 0
            if S[i] == '(':
                ll = 1
            elif S[i] == ')':
                rr = 1

            if o > 0 and rr:
                helper(i+1, s+S[i], l, r+1, o-1)
            if o >= 0 and ll:
                helper(i+1, s+S[i], l+1, r, o+1)

            if not ll and not rr:
                helper(i+1, s+S[i], l, r, o)
            else:
                helper(i+1, s, l, r, o)

        helper(0, '', 0, 0, 0)
        return list(valid) if len(valid) else [""]



cases = [
"(a)())()",
'()',
')(',
")(f",
")()(",
")()",
"a)())()",
"",
" ",
"(",
")",
"()())"
]
for case in cases:
    print(case, Solution().removeInvalidParentheses(case))
    print('========================================')
