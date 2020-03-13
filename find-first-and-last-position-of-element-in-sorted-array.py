from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        if len(nums) == 0:
            return ans

        lo, hi = 0, len(nums) - 1

        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if nums[mid-1] < target:
                lo = mid
            else:
                hi = mid

        if nums[lo] == target:
            ans[0] = lo

        lo, hi = 0, len(nums) - 1
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if nums[mid+1] <= target:
                lo = mid
            else:
                hi = mid

        if nums[hi] == target:
            ans[1] = hi

        if ans[0] == -1 and ans[1] != -1:
            ans[0] = ans[1]
        if ans[1] == -1 and ans[0] != -1:
            ans[1] = ans[0]

        return ans

    


import unittest

class Test(unittest.TestCase):

    def test1(self):
        nums = [5,7,7,8,8,10]
        target = 8
        self.assertListEqual(Solution().searchRange(nums, target), [3, 4])
    
    def test2(self):
        nums = [5,7,7,8,8,10]
        target = 6
        self.assertListEqual(Solution().searchRange(nums, target), [-1, -1])

    def test3(self):
        nums = [5,7,7,8,8,10]
        target = 5
        self.assertListEqual(Solution().searchRange(nums, target), [0, 0])

    def test4(self):
        #               |
        nums = [5,7,7,8,8,8,8,9,10]
        target = 8
        self.assertListEqual(Solution().searchRange(nums, target), [3, 6])

    def test5(self):
        nums = [5,7,7,8,8,10]
        target = 10
        self.assertListEqual(Solution().searchRange(nums, target), [5,5])

    def test6(self):
        nums = [2, 2]
        target = 2
        self.assertListEqual(Solution().searchRange(nums, target), [0, 1])
    
    def test6(self):
        nums = [2]
        target = 2
        self.assertListEqual(Solution().searchRange(nums, target), [0, 0])

unittest.main(exit=False)
