import math

class Solution:
    def uniquePaths_math(self, m: int, n: int) -> int:
        m -= 1
        n -= 1
        return int(math.factorial(m + n) / (math.factorial(m) * math.factorial(n)))

    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[1] * m for _ in range(n)]
        for r in range(1, n):
            for c in range(1, m):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[-1][-1]

import unittest

class Test(unittest.TestCase):

    def test1(self):
        m, n = 3, 2
        self.assertEqual(Solution().uniquePaths(m, n), 3)

    def test2(self):
        m, n = 7, 3
        self.assertEqual(Solution().uniquePaths(m, n), 28)

    def test3(self):
        m = n = 31
        self.assertEqual(Solution().uniquePaths(m, n), Solution().uniquePaths_math(m, n))


unittest.main(exit=False)

#  2275088307942293 4966181954039568885395604168260154104734000
#  2275088307942293 5138508509184433581249481632457411272900608
