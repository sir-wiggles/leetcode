import unittest

class Solution:
    def myAtoi(self, str: str) -> int:
        n = str.strip().split(' ')[0]
        s = 1

        MAX = 2 ** 31 - 1
        MIN = -2 ** 31

        digits = []
        for i, c in enumerate(n):
            if i == 0:
                if c == '-':
                    s = -1
                    continue
                elif c == '+':
                    continue
            if c.isdigit():
                digits.append(c)
            else:
                break

        if len(digits) == 0:
            return 0
        n = s * int(''.join(digits))
        if n >= MAX:
            return MAX
        elif n <= MIN:
            return MIN
        return n


class Test(unittest.TestCase):

    def test_number(self):
        assert Solution().myAtoi("42") == 42

    def test_leading_spaces(self):
        assert Solution().myAtoi("    42") == 42

    def test_with_sign(self):
        assert Solution().myAtoi("+42") == 42
    
    def test_with_negative_sign(self):
        assert Solution().myAtoi("-42") == -42

    def test_with_lagging_letters(self):
        assert Solution().myAtoi("-42abc") == -42

    def test_with_leading_letters(self):
        assert Solution().myAtoi("a-42") == 0

    def test_large_number(self):
        assert Solution().myAtoi(str(2 ** 31 - 1)) == 2 ** 31 - 1
        assert Solution().myAtoi(str(2 ** 31 - 1 + 1)) == 2 ** 31 - 1
        assert Solution().myAtoi(str(2 ** 31 - 1 - 1)) == 2 ** 31 - 1 - 1

    def test_small_number(self):
        assert Solution().myAtoi(str(-2 ** 31)) == -2 ** 31 
        assert Solution().myAtoi(str(-2 ** 31 - 1)) == -2 ** 31 
        assert Solution().myAtoi(str(-2 ** 31 + 1)) == -2 ** 31 +1




unittest.main(exit=False)
