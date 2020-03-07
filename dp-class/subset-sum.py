from typing import List
from pudb import set_trace

class SubsetSum:

    def bf(self, nums: List[int], target: int, index: int = 0) -> bool:

        if target == 0:
            return True

        if index >= len(nums):
            return False

        if nums[index] <= target:
            if self.bf(nums, target - nums[index], index + 1):
                return True

        return self.bf(nums, target, index + 1)

    def dp(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False

        dp = [
            [False for _ in range(target+1)] for _ in nums
        ]

        for i in range(len(dp)):
            dp[i][0] = True

        for i in range(1, target+1):
            dp[0][i] = nums[0] == i

        for i in range(1, len(dp)):
            for j in range(1, target+1):
                if dp[i-1][j]:
                    dp[i][j] = dp[i-1][j]
                elif nums[i] <= target:
                    dp[i][j] = dp[i-1][j - nums[i]]

        return dp[-1][-1]


test = [1, 2, 3, 7]
target = 6
assert SubsetSum().dp(test, target) == True

test = []
target = 6
assert SubsetSum().dp(test, target) == False

test = [1]
target = 6
assert SubsetSum().dp(test, target) == False

test = [1]
target = 1
assert SubsetSum().dp(test, target) == True


