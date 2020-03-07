from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:

        return not (
            # if the right most side of R1 is less than R2 
            rec1[2] <= rec2[0] or  # left
            rec1[0] >= rec2[2] or  # right
            rec1[1] >= rec2[3] or  # top
            rec1[3] <= rec2[1]     # bottom
        )    

rec1 = [0,0,2,2]
rec2 = [-1,1,0,3]


#  rec1 = [0,0,1,1]
#  rec2 = [1,0,2,1]


rec1 = [2,17,6,20]
rec2 = [3,8,6,20]

print(Solution().isRectangleOverlap(rec1, rec2))
