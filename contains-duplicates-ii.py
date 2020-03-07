from typing import List
from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = defaultdict(list)

        for i, n in enumerate(nums):
            m[n].append(i)

        for _, v in m.items():
            if len(v) > 1:
                i, j = 0, 1
                while j < len(v):
                    if k >= v[j] - v[i]:
                        return True
                    i += 1
                    j += 1
        return False

print(Solution().containsNearbyDuplicate([1, 2, 3, 1], 3))
