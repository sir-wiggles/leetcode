from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, n in enumerate(nums):
            missing ^= i ^ n
        return missing


t = [3, 0, 1]
#  t = [9,6,4,2,3,5,7,0,1]
print(Solution().missingNumber(t))
