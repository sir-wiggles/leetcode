from typing import List
from functools import lru_cache

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        end = len(height) - 1

        # find the highest point and its index, this will be the piviot
        hi, h = max(enumerate(height), key=lambda x: x[1])

        # calculate the total volume of the area in question
        volume = (end + 1) * h

        # calculate all the white space to the left of the highest point
        i = j = 0
        left = 0
        while j <= hi:
            if height[i] < height[j]:
                left += (height[j] - height[i]) * j
                i = j
            else:
                j += 1

        # calculate all the white space to the right of the highest point
        i = j = end
        right = 0
        while i >= hi:
            if height[i] > height[j]:
                right += (height[i] - height[j]) * (end - i)
                j = i
            else:
                i -= 1

        # the total rain is the total volume minus the spaces where water
        # can't be 
        return (volume - (left + right + sum(height)))

#    0 1 2 3 4 5 6 7 8 9 0 1
cases = [[0,1,0,2,1,0,1,3,2,1,2,1],
[1, 0, 1],
[2, 0, 1],
[1, 0, 2],
[2, 1, 2],
[2, 0, 2],
]
for case in cases:
    print(Solution().trap(case))
