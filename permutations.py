from typing import List

from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        output = []
        def helper(i):
            if i == len(nums):
                output.append(nums[:])
            for j, _ in enumerate(nums[i:], start=i):
                nums[i], nums[j] = nums[j], nums[i]
                helper(i+1)
                nums[i], nums[j] = nums[j], nums[i]
        helper(0)
        return output



print(Solution().permute([1, 2, 3]))
        
