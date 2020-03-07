from typing import List
from queue import deque

from queue import deque

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:

        stack = deque([(0, 0)])
        seen = {}

        total = 0
        while stack:
            i, s = stack.pop()

            if s == S and i == len(nums):
                total += 1
            elif i < len(nums):

                if (i+1, s + nums[i] + 1000) not in seen:
                    stack.append((i + 1, s + nums[i]))
                    seen[(i, s + nums[i] + 1000)] = True

                if (i+1, s - nums[i] + 1000) not in seen:
                    stack.append((i + 1, s - nums[i]))
                    seen[(i, s + nums[i] - 1000)] = True


        return total

a = [7,46,36,49,5,34,25,39,41,38,49,47,17,11,1,41,7,16,23,13]
s = 3
print(Solution().findTargetSumWays(a, s))
