from typing import List
import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            '*': operator.mul,
            '/': operator.truediv,
            '+': operator.add,
            '-': operator.sub
        }
        tokens = tokens[::-1]
        while tokens:
            token = tokens.pop()
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                stack.append(int(operators[token](a, b)))
                continue
            stack.append(int(token))
        return stack.pop()

print(Solution().evalRPN(["2", "1", "+", "3", "*"]))
print(Solution().evalRPN(["4", "13", "5", "/", "+"]))
print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
