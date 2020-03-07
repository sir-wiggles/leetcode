from collections import deque
from typing import List

inf = 2 ** 31 - 1

class Solution:

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        maxr = len(rooms)
        if maxr == 0:
            return
        maxc = len(rooms[0])

        def search(r, c):
            neighbors = [ (1, 0), (-1, 0), (0, 1), (0, -1) ]

            queue = deque(  [( r, c, [(r, c)] )]  )
            seen = set()

            while queue:
                node = queue.popleft()
                r, c, path = node

                if rooms[r][c] < 0:
                    for count, (r, c) in enumerate(path[::-1][1:], start=1):
                        rooms[r][c] = count
                    return

                seen.add((r, c))

                for (dr, dc) in neighbors:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nc < 0 or nr >= maxr or nc >= maxc:
                        continue
                    if (nr, nc) in seen or rooms[nr][nc] == -1:
                        continue

                    queue.append((nr, nc, path + [(nr, nc)]))

        for r, row in enumerate(rooms):
            for c, cell in enumerate(row):
                if cell > 0:
                    search(r, c)

rooms = [
    [inf,  -1,   0, inf],
    [inf, inf, inf,  -1],
    [inf,  -1, inf,  -1],
    [0  ,  -1, inf, inf]
]
Solution().wallsAndGates(rooms)

for row in rooms:
    print(row)
