from typing import List
import math

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda x: math.hypot(*x))
        return points[:K]

i = [[3,3],[5,-1],[-2,4]]
K = 2

print(Solution().kClosest(i, K))
