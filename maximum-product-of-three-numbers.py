from typing import List
from functools import reduce

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return max(
            reduce(lambda x, y: x*y, nums[-3:]), 
            reduce(lambda x, y: x*y, [nums[0], nums[1], nums[-1]])
        )

t = [-10,-1, 1,2,3]
print(Solution().maximumProduct(t))
