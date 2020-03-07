
class Solution:
    def removeOuterParentheses(self, S: str) -> str:

        stack = []
        paren_open = 0
        paren_closed = 0
        res = []
        for c in S:
            if c == '(':
                paren_open += 1
            elif c == ')':
                paren_closed += 1
            stack.append(c)

            if paren_open == paren_closed:
                res.append(''.join(stack[1:-1]))
                paren_open = 0
                paren_closed = 0
                stack = []
        return ''.join(res)




s = "(()())(())"
s = "(()())(())(()(()))"
print(Solution().removeOuterParentheses(s))
