from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i, m in enumerate(flowerbed):
            if m == 0 and (i==0 or flowerbed[i-1] == 0) and (i==len(flowerbed)-1 or flowerbed[i+1]==0):
                n -= 1
                flowerbed[i] = 1
        return n <= 0
    
import unittest

class Test(unittest.TestCase):

    def test1(self):
        i = [1,0,1, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 1, 0, 0]
        n = 8
        self.assertEqual(Solution().canPlaceFlowers(i, n), True)
    def test2(self):
        i = [1,0,0,0,0,0,1]
        n = 2
        self.assertEqual(Solution().canPlaceFlowers(i, n), True)
    def test3(self):
        i = [0,0,1]
        n = 1
        self.assertEqual(Solution().canPlaceFlowers(i, n), True)
    def test4(self):
        i = [1,0,0]
        n = 1
        self.assertEqual(Solution().canPlaceFlowers(i, n), True)
    def test5(self):
        i = [0,0,0]
        n = 2
        self.assertEqual(Solution().canPlaceFlowers(i, n), True)
    def test6(self):
        i = [1,0,0,0,0,1]
        n = 2
        self.assertEqual(Solution().canPlaceFlowers(i, n), False)


unittest.main(exit=False)
