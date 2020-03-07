from typing import List
from functools import reduce

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:

        count, satasified, window_maximum = 0, 0, -float('inf')
        for i, (c, g) in enumerate(zip(customers, grumpy)):
            if g == 0:
                satasified += c
            count += c * g
            if i >= X:
                count -= customers[i-X] * grumpy[i-X]
            window_maximum = max(window_maximum, count)

        return satasified + window_maximum






        



customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
X = 3
print(Solution().maxSatisfied(customers, grumpy, X))
