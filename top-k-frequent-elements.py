from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        return heapq.nlargest(k, freq.keys(), key=freq.get)

            

            

nums = [1, 1, 1, 2, 2, 3]
nums = [-1, -1]
k = 1
print(Solution().topKFrequent(nums, k))
