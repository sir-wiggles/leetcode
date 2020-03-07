import math

class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()
        import pudb; pudb.set_trace()
        while n != 1:

            power = int(math.log10(n))

            digits = []
            for p in range(power, -1, -1):
                digits.append(n // 10**p)
                n %= 10**p

            n = sum(map(lambda x: x**2, digits))
            if n in seen:
                return False
            seen.add(n)

        return True


print(Solution().isHappy(19))
