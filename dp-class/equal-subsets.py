from typing import List
from pudb import set_trace

'''
for each number 'i'
  create a new set which INCLUDES number 'i' if it does not exceed 'S/2', and recursively
      process the remaining numbers
  create a new set WITHOUT number 'i', and recursively process the remaining items
return true if any of the above sets has a sum equal to 'S/2', otherwise return false
'''

class EqualSubsets:

    def __init__(self):
        self.mem = {}

    def _solve(self, numbers: List[int], sum: int, index: int) -> bool:
        if sum == 0:
            return True

        if index >= len(numbers):
            return False

        res = False
        if numbers[index] <= sum:
            res = self._solve(numbers, sum-numbers[index], index+1)
            self.mem[(sum, index)] = res
            if res:
                return res

        res = self._solve(numbers, sum, index+1)
        self.mem[(sum, index)] = res
        return res

    def bruteforce(self, numbers: List[int]) -> bool:
        s = sum(numbers)
        if len(numbers) == 0 or s % 2:
            return False
        s //= 2
        return self._solve(numbers, s, 0)

    def dp(self, numbers: List[int]) -> bool:

        s = sum(numbers)
        n = len(numbers)
        m = s // 2

        if s % 2 != 0:
            return False

        dp = [[False for _ in range(m + 1)] for _ in range(n)]

        for r in dp:
            r[0] = True

        for i in range(m+1):
            dp[0][i] = i <= numbers[0]

        for r in dp:
            print(r)
        print()

        for i in range(1, n):
            for j in range(1, m+1):
                if dp[i-1][j]:
                    dp[i][j] = dp[i-1][j]
                elif j >= numbers[i]:
                    dp[i][j] = dp[i-1][j - numbers[i]]

        for r in dp:
            print(r)
        return dp[-1][-1]


test = [1, 1, 10]
assert EqualSubsets().dp(test) is True

test = [1, 3, 2, 6]
assert EqualSubsets().bruteforce(test) is True

test = [1, 3, 2]
assert EqualSubsets().bruteforce(test) is True

test = [1, 2, 3, 4]
assert EqualSubsets().bruteforce(test) is True

test = []
assert EqualSubsets().bruteforce(test) is False

test = [1]
assert EqualSubsets().bruteforce(test) is False

test = [1, 1]
assert EqualSubsets().bruteforce(test) is True

test = [1, 0]
assert EqualSubsets().bruteforce(test) is False

test = [0, 1]
assert EqualSubsets().bruteforce(test) is False

test = [1, 1, 3, 4, 7]
assert EqualSubsets().bruteforce(test) is True

test = [1] * 100
assert EqualSubsets().bruteforce(test) is True

test = [0] * 2
assert EqualSubsets().bruteforce(test) is True

test = list(range(101))
assert EqualSubsets().bruteforce(test) is True
