from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        final = []
        for curr in asteroids:
            while final and curr < 0 < final[-1]:
                if final[-1] < abs(curr):
                    final.pop()
                    continue
                elif final[-1] == abs(curr):
                    final.pop()
                break
            else:
                final.append(curr)
        return final





import unittest
class Test(unittest.TestCase):

    def test1(self):
        i = [5, 10, -5]
        o = [5, 10]
        self.assertListEqual(Solution().asteroidCollision(i), o)

    def test2(self):
        i = [10, -20]
        o = [-20]
        self.assertListEqual(Solution().asteroidCollision(i), o)

    def test3(self):
        i = [20, -10]
        o = [20]
        self.assertListEqual(Solution().asteroidCollision(i), o)

    def test4(self):
        i = [20, -20]
        o = []
        self.assertListEqual(Solution().asteroidCollision(i), o)

    def test5(self):
        i = [-1, 5, 10, -5]
        o = [-1, 5, 10]
        self.assertListEqual(Solution().asteroidCollision(i), o)

    def test6(self):
        i = [-20, 20]
        o = [-20, 20]
        self.assertListEqual(Solution().asteroidCollision(i), o)

    def test7(self):
        i = [-1, 5, -1, -10, -1, 10, -5]
        o = [-1, -10, -1, 10]
        self.assertListEqual(Solution().asteroidCollision(i), o)

    def test8(self):
        i = [-1, 10, 5, -1, -10, -1, 10, -5]
        o = [-1, -1, 10]
        self.assertListEqual(Solution().asteroidCollision(i), o)

    def test9(self):
        i = []
        o = []
        self.assertListEqual(Solution().asteroidCollision(i), o)

    def test10(self):
        i = [-2, -1, 1, 2]
        o = [-2, -1, 1, 2]
        self.assertListEqual(Solution().asteroidCollision(i), o)

    def test11(self):
        i = [10, 2, -5]
        o = [10]
        self.assertListEqual(Solution().asteroidCollision(i), o)


unittest.main(exit=False)
