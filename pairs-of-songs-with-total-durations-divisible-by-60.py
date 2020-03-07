from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # array of remainders 
        r = [0] * 60
        c = 0
        for t in time:
            # add the count of the compliment remainder
            c += r[-t % 60]
            # inc the remainder
            r[t % 60] += 1
        return c




t = [30,20,150,100,40]
#  t = [60,60,60]
#  t = [30, 20]
#  t = range(0, 60000, 70)
print(Solution().numPairsDivisibleBy60(t))
