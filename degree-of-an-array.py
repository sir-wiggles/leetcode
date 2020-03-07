from typing import List
from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        m = defaultdict(list)

        maximum = float('-inf')
        for i, n in enumerate(nums):
            m[n].append(i)
            if len(m[n]) > maximum:
                maximum = len(m[n])

        longest = float('inf')
        for v in m.values():
            if len(v) == maximum:
                longest = min(longest, v[-1] - v[0] + 1)

        return longest



t = [1, 2, 2, 3, 1]
t = [1,2,2,3,1,4,2]
t = [2,1,1,2,1,3,3,3,1,3,1,3,2]
print(Solution().findShortestSubArray(t))
