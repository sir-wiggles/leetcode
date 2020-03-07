from typing import List
from functools import lru_cache

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        possible = []
        def generate(s, l=0, r=0):
            if l < n:
                generate(s + '(', l+1, r)
            if r < l:
                generate(s + ')', l, r+1)
            if l + r == 2 * n:
                possible.append(s)
        generate('')
        return possible


for r in Solution().generateParenthesis(4):
    print(r)
