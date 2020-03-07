from typing import List
from functools import lru_cache


class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        inf = float('inf')
        
        @lru_cache(None)
        def helper(i, swapped):
            if i == len(A):
                return 0

            a = inf 
            if not (i > 0 and (A[i - 1] >= A[i] or B[i - 1] >= B[i])):
                a = helper(i + 1, 0)

            b = inf 
            A[i], B[i] = B[i], A[i]
            if not (i > 0 and (A[i - 1] >= A[i] or B[i - 1] >= B[i])):
                b = helper(i + 1, 1)
            A[i], B[i] = B[i], A[i]

            return min(a, b + 1)

        if len(A) == 1: 
            return 0
        return helper(0, 0)

a = [1,2,6,7]
b = [1,2,7,6]

#  a = [3,3,8,9,10]
#  b = [1,7,4,6,8]

#  a = [3,3,8,6,10]
#  b = [1,7,4,9,8]

#  a = [1,3,5,4]
#  b = [1,2,3,7]

#  a = [0,3,5,8,9]
#  b = [2,1,4,6,9]
print(Solution().minSwap(a, b))
