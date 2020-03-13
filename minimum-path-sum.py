from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        maxr = len(grid)
        maxc = len(grid[0])

        inf = float('inf')
        dp = [[inf] * (maxc+1) for _ in range(maxr+1)]
        dp[0][1] = 0
        dp[1][0] = 0

        for r, row in enumerate(grid, start=1):
            for c, cell in enumerate(row, start=1):
                dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + cell
        return dp[-1][-1]


        

i = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

i = [
    [1,4,8,6,2,2,1,7],
    [4,7,3,1,4,5,5,1],
    [8,8,2,1,1,8,0,1],
    [8,9,2,9,8,0,8,9],
    [5,7,5,7,1,8,5,5],
    [7,0,9,4,5,6,5,6],
    [4,9,9,7,9,1,9,0]
]

print(Solution().minPathSum(i))
