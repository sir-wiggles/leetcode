from typing import List
from collections import deque

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        maxr = len(matrix)
        if maxr == 0:
            return False
        maxc = len(matrix[0])

        r, c = maxr-1, 0
        while 0 <= r < maxr and 0 <= c < maxc:
            if target < matrix[r][c]:
                r -= 1
            elif target > matrix[r][c]:
                c += 1
            else:
                return True
        return False


i = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
targets = [ 5, 20 ]

for case in targets:
    print(Solution().searchMatrix(i, case))
