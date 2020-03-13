from typing import List
from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        curr, p0, p2 = 0, 0, len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                swap(curr, p0)
                curr += 1
                p0 += 1
            elif nums[curr] == 2:
                swap(curr, p2)
                p2 -= 1
            else:
                curr += 1



import unittest
class Test(unittest.TestCase):

    def test1(self):
        i = [2,0,2,1,1,0]
        Solution().sortColors(i)
        self.assertListEqual(i, sorted(i))

    def test2(self):
        i = [0,1,1,2,0,2]
        Solution().sortColors(i)
        self.assertListEqual(i, sorted(i))

    def test3(self):
        i = [2,0,1]
        Solution().sortColors(i)
        self.assertListEqual(i, sorted(i))

    def test4(self):
        #              | |
        i = [2,1,0,0,1,1,2,2,0,0,1,0]
        Solution().sortColors(i)
        self.assertListEqual(i, sorted(i))

unittest.main(exit=False)
