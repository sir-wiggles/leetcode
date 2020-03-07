from typing import List
from functools import lru_cache

class Solution:
    def solve(self, nums: List[int]) -> bool:

        def helper(i, s):
            if s == 0:
                return True
            # we're at the end and we haven't found a valid partition
            elif i >= len(nums):
                return False

            # add values to the left side while keeping the right side the same
            # and then add values to the right si
            return helper(i+1, s-nums[i]) or helper(i+1, s)

        target = sum(nums) 
        if target % 2 != 0:
            return False
        return helper(0, target//2)

    def printdb(self, dp, nums):
        print('  ', '  '.join(map(str, range(0, sum(nums)+1))))
        for i, r in enumerate(dp):
            print(nums[i], r)

        print('=========================================')

    def dp(self, nums: List[int]) -> bool:
        
        dp = [[0 for _ in range(sum(nums)+1)] for n in nums]

        self.printdb(dp, nums)
        for row in dp:
            row[0] = 1

        self.printdb(dp, nums)
            
        for i, row in enumerate(dp):
            for j, cell in enumerate(row):
                # if we can get the sum 'j' without the number at index 'i'
                #  print(f'number: {nums[i]} sum: {j}')
                if dp[i-1][j]:
                    #  print('dp[i-1][j]')
                    dp[i][j] = dp[i-1][j]

                # else if we can find a subset to get the remaining sum
                elif j >= nums[i]:
                    #  print('dp[i-1][j-nums[i]]')
                    dp[i][j] = dp[i-1][j-nums[i]]

                #  self.printdb(dp, nums)
                #  input()

        self.printdb(dp, nums)
        return True if dp[-1][-1] else False





test = [1, 1, 3, 4]
print(Solution().dp(test))
print(Solution().solve(test))
