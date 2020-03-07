from typing import List

from collections import Counter

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = Counter(nums)

        keys = sorted(count.keys(), reverse=True)

        remaining = len(nums)
        for key in keys:
            remaining -= count[key]
            count[key] = remaining

        for i, n in enumerate(nums):
            nums[i] = count[n]
        return nums
            


        


nums = [8, 1, 2, 2, 3]
print(Solution().smallerNumbersThanCurrent(nums))
