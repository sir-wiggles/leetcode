from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        A = grid

        R, C = len(grid), len(grid[0])

        # queue - all starting cells with rotting oranges
        queue = deque()
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                if val == 2:
                    queue.append((r, c, 0))

        def neighbors(r, c):
            for nr, nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        d = 0
        while queue:
            r, c, d = queue.popleft()
            for nr, nc in neighbors(r, c):
                if A[nr][nc] == 1:
                    A[nr][nc] = 2
                    queue.append((nr, nc, d+1))

        if any(1 in row for row in A):
            return -1
        return d



        
t = [[2,1,1],[1,1,0],[0,1,1]]
print(Solution().orangesRotting(t))

t = [[2,1,1],[0,1,1],[1,0,1]]
print(Solution().orangesRotting(t))

t = [[0,2]]
print(Solution().orangesRotting(t))

t = [[2,1,0,2]]
print(Solution().orangesRotting(t))

t = [[1,2]]
print(Solution().orangesRotting(t))

t = [[2,1,0,2]]
print(Solution().orangesRotting(t))
