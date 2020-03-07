from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0

        def isMagic(r, c):

            digits = set()
            for i in range(-1, 2):
                for j in range(-1, 2):
                    digits.add(grid[r+i][c+j])

            if len(digits) != 9:
                return 0
            if max(digits) != 9 and min(digits) != 1:
                return 0

            d1 = grid[r-1][c-1] + grid[r+1][c+1] + grid[r][c]
            d2 = grid[r+1][c-1] + grid[r-1][c+1] + grid[r][c]

            v1 = grid[r-1][c-1] + grid[r][c-1] + grid[r+1][c-1]
            v2 = grid[r-1][c-0] + grid[r][c-0] + grid[r+1][c-0]
            v3 = grid[r-1][c+1] + grid[r][c+1] + grid[r+1][c+1]

            h1 = sum(grid[r-1][c-1:c+2])
            h2 = sum(grid[r+0][c-1:c+2])
            h3 = sum(grid[r+1][c-1:c+2])

            if len(set((h1, h2, h3, v1, v2, v3, d1, d2))) == 1:
                return 1
            return 0

        count = 0
        for r, row in enumerate(grid[1:-1], start=1):
            for c, cell in enumerate(row[1:-1], start=1):
                if cell == 5:
                    count += isMagic(r, c)

        return count






i = [
    [4,3,8,4], 
    [9,5,1,9], 
    [2,7,6,2],
    [2,7,6,2],
    [9,5,1,9], 
    [4,3,8,4], 
]
i = [[1,8,6],[10,5,0],[4,2,9]]
print(Solution().numMagicSquaresInside(i))
