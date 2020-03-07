import math


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(math.sqrt(n)) + 1):
            if primes[i]:
                primes[i*i: n: i] = [False] * len(primes[i*i: n: i])
        return sum(primes)

cases = range(11)
for i, case in enumerate(cases):
    print(i, Solution().countPrimes(case))
