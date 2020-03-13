from typing import List
from functools import lru_cache
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        length = 0
        for n in nums:
            i = bisect.bisect_left(dp, n, 0, length)
            dp[i] = n
            if i == length:
                length += 1
        return length

    def lengthOfLIS_dp(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        maxans = 1
        for i, m in enumerate(nums):
            maxval = 0
            for j, n in enumerate(nums[:i]):
                if n < m:
                    maxval = max(maxval, dp[j])
            dp[i] = maxval + 1
            maxans = max(maxans, dp[i])
        return maxans

    def lengthOfLIS_brute_force(self, nums: List[int]) -> int:
        @lru_cache(None)
        def helper(i, p, c):
            if i == len(nums):
                return c
            count = 0
            if p < nums[i]:
                count = helper(i+1, nums[i], c+1)
            return max(count, helper(i+1, p, c))
        return helper(0, -float('inf'), 0)




import unittest

class Test(unittest.TestCase):

    def test1(self):
        i = [10,9,2,5,3,7,101,18,19,20]
        self.assertEqual(Solution().lengthOfLIS(i), 6)

    def test2(self):
        i = [2,2]
        self.assertEqual(Solution().lengthOfLIS(i), 1)

unittest.main(exit=False)
