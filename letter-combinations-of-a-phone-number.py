from typing import List
from functools import lru_cache

class Solution:
    m = {
            '0': ' ',
            '1': [''],
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
    }
    def letterCombinations(self, digits: str) -> List[str]:
        digits = digits.strip()
        if len(digits) == 0:
            return []
        for c in digits:
            if c == '0' or c == '1':
                return []

        @lru_cache(None)
        def helper(i, char):
            if i == len(digits):
                return char
            res = []
            for c in self.m[digits[i]]:
                for s in helper(i+1, c):
                    res.append(char + s)
            return res

        res = helper(0, '')
        return res


print(Solution().letterCombinations(''))
print(Solution().letterCombinations(' '))
print(Solution().letterCombinations('0'))
print(Solution().letterCombinations('1'))
print(Solution().letterCombinations('2'))
print(Solution().letterCombinations('3'))
print(Solution().letterCombinations('4'))
print(Solution().letterCombinations('5'))
print(Solution().letterCombinations('6'))
print(Solution().letterCombinations('7'))
print(Solution().letterCombinations('8'))
print(Solution().letterCombinations('9'))
print(Solution().letterCombinations('23'))

