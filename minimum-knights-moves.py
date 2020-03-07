from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:

        moves = [

            # Q 1
            ( 2,  1),
            ( 1,  2),

            #  # Q 4
            ( 2, -1),
            ( 1, -2),

            # Q 2
            (-2,  1),
            (-1,  2),

            #  # Q 3
            (-2, -1),
            (-1, -2),


        ]

        fx = abs(x)
        fy = abs(y)

        queue = deque([[0, 0, 0]])
        seen = set()

        while queue:

            x, y, m = queue.popleft()

            if (x, y) in seen:
                continue
            seen.add((x, y))

            if x == fx and y == fy:
                return m


            if abs(fx - x) < 10 or abs(fy - x) < 10:
                for (dx, dy) in moves:
                    queue.append([x+dx, y+dy, m+1])
            else:
                for (dx, dy) in moves[:4]:
                    queue.append([x+dx, y+dy, m+1])



print(Solution().minKnightMoves(0, 300))
