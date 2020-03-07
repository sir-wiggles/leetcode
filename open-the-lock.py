from typing import List
from queue import deque


class Solution:
    numbers = {
        '0': ['1', '9'],
        '1': ['2', '0'],
        '2': ['3', '1'],
        '3': ['4', '2'],
        '4': ['5', '3'],
        '5': ['6', '4'],
        '6': ['7', '5'],
        '7': ['8', '6'],
        '8': ['9', '7'],
        '9': ['0', '8'],
    }

    def openLock(self, deadends: List[str], target: str) -> int:
        start = list('0000')
        start.append(0)
        start = tuple(start)
        queue = deque([tuple(start)])

        dead = {}
        for deadend in deadends:
            dead[deadend] = True

        seen = {}

        while len(queue):
            node = queue.popleft()

            nodeStr = ''.join(node[:-1])
            if nodeStr in dead:
                continue

            if nodeStr == target:
                return node[-1]

            for i, digit in enumerate(node[:-1]):
                neighbors = self.numbers[digit]

                upper = [ node[0], node[1], node[2], node[3], node[4] + 1 ]
                lower = upper[:]

                upper[i] = neighbors[0]
                lower[i] = neighbors[1]

                upper = tuple(upper)
                lower = tuple(lower)

                upperStr = ''.join(upper[:-1])
                lowerStr = ''.join(lower[:-1])

                if upperStr not in seen:
                    seen[upperStr] = True
                    queue.append(upper)

                if lowerStr not in seen:
                    seen[lowerStr] = True
                    queue.append(lower)

        return -1

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
#  deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
#  target = "8888"
deadends = ["0000"]
target = '8888'
print(Solution().openLock(deadends, target))
