from typing import List
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        remaining = Counter(hand)
        import pudb; pudb.set_trace()

        for h in sorted(hand):
            for i in range(h, h+W):
                if i not in remaining:
                    return False

                if remaining[i] == 1:
                    remaining.pop(i)
                else:
                    remaining[i] -= 1
        return True

        #  while len(remaining) >= W:
            #  smallest = min([k for k in remaining])
            #  hand = Counter(range(smallest, smallest+W))
            #  remaining = remaining - hand
        #  else:
            #  if 0 < len(remaining) < W:
                #  return False
        #  return True

        
        

import unittest

class Test(unittest.TestCase):

    def test1(self):
        hand = [1,2,3,6,2,3,4,7,8]
        W = 3
        self.assertEqual(Solution().isNStraightHand(hand, W), True)

    def test2(self):
        hand = [1,2,3,4,5]
        W = 4
        self.assertEqual(Solution().isNStraightHand(hand, W), False)


unittest.main(exit=False)
