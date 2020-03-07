from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        s1, s2 = 0, 0
        for n in cost:
            s1, s2 = min(s1, s2) + n, s1
        return min(s1, s2)
    
    
    
import unittest

class Test(unittest.TestCase):

    def test1(self):
        cost = []
        self.assertEqual(Solution().minCostClimbingStairs(cost), 0)

    def test2(self):
        cost = [1]
        self.assertEqual(Solution().minCostClimbingStairs(cost), 0)

    def test3(self):
        cost = [1, 0]
        self.assertEqual(Solution().minCostClimbingStairs(cost), 0)

    def test4(self):
        cost = [1, 0, 1]
        self.assertEqual(Solution().minCostClimbingStairs(cost), 0)

    def test5(self):
        cost = [1, 2, 3]
        self.assertEqual(Solution().minCostClimbingStairs(cost), 2)

    def test6(self):
        cost = [1, 2, 3]
        self.assertEqual(Solution().minCostClimbingStairs(cost), 2)

    def test7(self):
        cost = [1, 2, 3, 4]
        self.assertEqual(Solution().minCostClimbingStairs(cost), 4)

unittest.main(exit=False)
