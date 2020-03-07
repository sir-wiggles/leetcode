from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        rmax = [max(row) for row in grid]
        cmax = [max(col) for col in zip(*grid)]

        change = 0
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                change += abs(cell - min(rmax[r], cmax[c]))
        
        return change

grid = [
#    9 4 8 7
    [3,0,8,4], # 8
    [2,4,5,7], # 7
    [9,2,6,3], # 9
    [0,3,1,0]  # 3
]
print(Solution().maxIncreaseKeepingSkyline(grid))

print([max(row) for row in grid])
print([max(row) for row in zip(*grid)])

