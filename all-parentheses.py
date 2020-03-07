from typing import List
from collections import deque

class Solution:

    def __init__(self):
        self.res = []
        self.seen = set()

    def check(self, s: str) -> bool:
        if len(s) == 0:
            return False

        stack = deque()
        for c in s:
            if c == ')' and len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            # no items in the stack with closing bracket can return now
            elif c == ')' and len(stack) == 0:
                return False
            else:
                stack.append(c)
        return len(stack) == 0

    def _solve(self, s, current='', index=0) -> List[str]:

        if current in self.seen:
            return

        if index == len(s):
            if self.check(current):
                self.res.append(current)
            return self.seen.add(current)

        self._solve(s, current+s[index], index+1)
        self._solve(s, current, index+1)

    def solve(self, s: str) -> List[str]:
        self._solve(s)
        return self.res

s = '(())'
print(Solution().solve(s))

