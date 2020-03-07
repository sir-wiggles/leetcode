from typing import List

class Solution:

    def bf(self, nums: List[int], sum1: int = 0, sum2: int = 0, index: int = 0) -> int:

        if index == len(nums):
            return abs(sum1 - sum2)

        a = self.bf(nums, sum1 + nums[index], sum2, index+1)
        b = self.bf(nums, sum1, sum2 + nums[index], index+1)
        return min(a, b)

test = [1, 2, 3, 9]
assert Solution().bf(test) == 3

test = [1, 2, 7, 1, 5]
assert Solution().bf(test) == 0
