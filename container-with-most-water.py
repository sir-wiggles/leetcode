from typing import List
from functools import lru_cache

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 1:
            return 0

        i, j = 0, len(height) - 1
        m = -float('inf')
        while i < j:
            m = max((j - i) * min(height[i], height[j]), m)
            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else: # equal
                i += 1 
                j -= 1 
        return m

i = [1,8,6,2,5,4,8,3,7]
i = [1,1]
print(Solution().maxArea(i))
