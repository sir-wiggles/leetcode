from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxp = minp = ans = nums[0]
        for n in nums[1:]:
            u, l = maxp * n, minp * n
            maxp = max(n, u, l)
            minp = min(n, u, l)
            ans = max(maxp, ans)
        return ans

    def maxProduct_brute_force(self, nums: List[int]) -> int:
        maximum = -float('inf')
        for i, n in enumerate(nums):
            product = n
            for j in range(i+1, len(nums)):
                product *= nums[j]
                maximum = max(maximum, product)
        return maximum


import unittest
class Test(unittest.TestCase):
    def test1(self):
        i = [2, 3, -2, 4]
        self.assertEqual(Solution().maxProduct(i), 6)

    def test2(self):
        i = [-2, 0, -1]
        self.assertEqual(Solution().maxProduct(i), 0)

    def test3(self):
        i = [2, 3, -2, 4, -1]
        self.assertEqual(Solution().maxProduct(i), 48)

    def test4(self):
        i = [2, 3, -2, -1, 0, -1]
        self.assertEqual(Solution().maxProduct(i), 12)

    def test5(self):
        i = [-2, 0, -1, -2]
        self.assertEqual(Solution().maxProduct(i), 2)

    def test6(self):
        i = [-2]
        self.assertEqual(Solution().maxProduct(i), -2)

    def test7(self):
        i = [3, -1, 4]
        self.assertEqual(Solution().maxProduct(i), 4)

    def test8(self):
        i = [0, 2]
        self.assertEqual(Solution().maxProduct(i), 2)


unittest.main(exit=False)
