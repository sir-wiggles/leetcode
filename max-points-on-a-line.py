from typing import List
import collections

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        answer = 0
        for px, py in points:
            pctr = 0
            ctr = collections.Counter()
            for qx, qy in points:
                x, y = qx - px, qy - py
                pctr += x == y == 0
                ctr[y/x if x else 'inf'] += 1
            ctr['inf'] -= pctr
            print(ctr)
            answer = max(answer, pctr + max(ctr.values()))
        return answer





import unittest
import random
class Test(unittest.TestCase):

    #  def test1(self):
        #  i = [[1,1],[2,2],[3,3]]
        #  self.assertEqual(Solution().maxPoints(i), 3)

    #  def test2(self):
        #  i = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
        #  self.assertEqual(Solution().maxPoints(i), 4)
    
    #  def test3(self):
        #  i = [[1,1],[1,2], [2,2],[3,3]]
        #  self.assertEqual(Solution().maxPoints(i), 3)

    #  def test4(self):
        #  i = sorted([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]])
        #  for x in range(10):
            #  random.shuffle(i)
            #  print(i)
            #  self.assertEqual(Solution().maxPoints(i[:]), 4)

    #  def test5(self):
        #  i = [[0,0]]
        #  self.assertEqual(Solution().maxPoints(i), 1)

    def test6(self):
        i = [[0,0],[94911151,94911150],[94911152,94911151]]
        self.assertEqual(Solution().maxPoints(i), 2)

    

unittest.main(exit=False)
