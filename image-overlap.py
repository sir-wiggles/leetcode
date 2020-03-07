from typing import List
from itertools import chain

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:

        a = list(chain(*A))
        b = list(chain(*B))

        maximum = -float('inf')
        for i in range(len(a)):
            maximum = max(maximum, sum(m&n for m, n in zip(a, b[i:])))

        for i in range(len(a)):
            maximum = max(maximum, sum(m&n for m, n in zip(b, a[i:])))

        return maximum

            

        




import unittest

class Test(unittest.TestCase):

    def test1(self):
        A = [[1,1,0],
             [0,1,0],
             [0,1,0]]
        B = [[0,0,0],
             [0,1,1],
             [0,0,1]]
        self.assertEqual(Solution().largestOverlap(A, B), 3)

    def test2(self):
        A = [[0,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,0,1],[0,1,0,0,1]]
        B = [[1,0,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[0,1,1,1,1],[1,0,1,1,1]]
        self.assertEqual(Solution().largestOverlap(A, B), 5)

    def test3(self):
        A = [[0,1],[1,1]]
        B = [[1,1],[1,0]]
        self.assertEqual(Solution().largestOverlap(A, B), 2)

unittest.main(exit=False)
