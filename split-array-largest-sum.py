from typing import List

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        if nums == []:
            return 0
        if m == 1:
            return sum(nums)

        min_result = float('inf')
        for j in range(1, len(nums)):
            left, right = sum(nums[:j]), self.splitArray(nums[j:], m-1)
            min_result = min(min_result, max(left, right))
        return min_result


test = [7, 2, 5, 10, 8]
m = 2
print(Solution().splitArray(test, m))
