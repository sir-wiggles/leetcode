from collections import deque
import math

class Solution:
    def numSquares(self, n: int) -> int:
        #  import pudb; pudb.set_trace()
        upper = int(math.sqrt(n))

        squares = [n**2 for n in range(1, upper+1)][::-1]

        queue = deque([(0, 0)])

        while queue:
            count, total = queue.popleft()

            for square in squares:
                newTotal = total + square
                if newTotal == n:
                    return count + 1
                queue.append((count+1, newTotal))

print(Solution().numSquares(61783))
