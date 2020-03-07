from typing import List
from queue import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        seen = [False] * len(rooms)
        numRooms = len(rooms)
        openedRooms = 0

        stack = deque([0])

        while stack:
            room = stack.popleft()

            if seen[room] == False:
                openedRooms += 1
                seen[room] = True
            else:
                continue

            if openedRooms == numRooms:
                return True

            keys = rooms[room]
            stack.extend(keys)

        return False





case = [[1],[2],[3],[]]
print(Solution().canVisitAllRooms(case))

case = [[1,3],[3,0,1],[2],[0]]
print(Solution().canVisitAllRooms(case))
