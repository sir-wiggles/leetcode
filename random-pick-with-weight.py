from typing import List
import random

# Simple way of thinking of this is to look at the following example.

# Given A, B and C I want A to show up 10%  B to show up 10% and C to show up
# the rest (80%).            1  1  |---------- 8 -------|
# If I make an array of a = [A, B, C, C, C, C, C, C, C, C] and random.choice(a)
# the result will be a weighted result.  

# We can't use this solution for this problem, it would be crazy to have a potential
# array which is why we sum.
# having 10000000 show up 10000000 is a bad solution
# [10000000, 1, 2, 3, 4]

class Solution:

    def __init__(self, w: List[int]):

        self.weights = w
        for i, w in enumerate(self.weights[1:], start=1):
            self.weights[i] += self.weights[i-1]
        self.total = self.weights[-1]

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        lo, hi = 0, len(self.weights)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.weights[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo

s = Solution([51, 49])
from collections import Counter
print(Counter([s.pickIndex() for x in range(1000000)]))
