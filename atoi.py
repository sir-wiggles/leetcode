class Solution:
    def myAtoi(self, str: str) -> int:
        a = 0
        try:
            a = int(str)
        except:
            return a
        if a > 2**32 - 1:
            return 2**32 - 1
        if a < -2**32:
            return -2**32
        return a


print(Solution().myAtoi('42'))
