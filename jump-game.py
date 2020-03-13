from typing import List

class Solution:
    def canJump_recursion_with_memo(self, nums: List[int]) -> bool:

        UNKNOWN, BAD, GOOD = -1, 0, 1
        memo = [UNKNOWN] * len(nums)
        memo[-1] = GOOD

        def helper(i):

            if i >= len(nums) - 1 :
                return True
            if memo[i] > UNKNOWN:
                return bool(memo[i])

            for j in range(nums[i], 0, -1):
                if helper(i+j):
                    memo[i] = GOOD
                    return True

            memo[i] = BAD
            return False
        return helper(0)
    
    def canJump_dp(self, nums: List[int]) -> bool:
        UNKNOWN, GOOD = -1, 1
        memo = [UNKNOWN] * len(nums)
        memo[-1] = GOOD

        i = len(nums) - 2
        while i >= 0:
            if nums[i] == 0:
                i -= 1
                continue
            furthest_jump = min(nums[i] + i, len(nums)-1)
            j = i + 1
            while j <= furthest_jump:
                if memo[j] == GOOD:
                    memo[i] = GOOD
                    break
                j += 1
            i -= 1

        return memo[0] == GOOD
    
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums) - 2
        last_good = len(nums) - 1
        while i >= 0:
            if i + nums[i] >= last_good:
                last_good = i
            i -= 1
        return last_good == 0



import unittest

class Test(unittest.TestCase):

    def test1(self):
        i = [2,3,1,1,4]
        self.assertEqual(Solution().canJump(i), True)

    def test2(self):
        i = [3,2,1,0,4] 
        self.assertEqual(Solution().canJump(i), False)

    def test3(self):
        i = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6] 
        self.assertEqual(Solution().canJump(i), False)

    def test4(self):
        i = [2,0] 
        self.assertEqual(Solution().canJump(i), True)


unittest.main(exit=False)
