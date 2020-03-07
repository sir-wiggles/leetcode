from typing import List
from queue import deque


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        maxr = len(matrix)
        maxc = len(matrix[0])

        def getNeighbors(r, c, i):
            moves = [ (1, 0), (-1, 0), (0, 1), (0, -1), ]
            for move in moves:
                dr, dc = move
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= maxr or nc < 0 or nc >= maxc or (nr, nc) in seen:
                    continue
                stack.append((nr, nc, i))

        for r, row in enumerate(matrix):
            for c, cell in enumerate(row):
                if cell == 0:
                    continue

                stack = deque()
                seen = set([(r, c)])
                stack.append((r, c, 0))

                while stack:
                    node = stack.popleft()
                    nr, nc, i = node
                    if matrix[nr][nc] == 0:
                        matrix[r][c] = i
                        stack = deque()
                        break
                    getNeighbors(nr, nc, i + 1)
        return matrix




matrix = [
 [0,0,0],
 [0,1,0],
 [1,1,1]
]
print(Solution().updateMatrix(matrix))

