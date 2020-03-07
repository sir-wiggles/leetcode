from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        final = set()
        def helper(i, s):
            if i == len(nums):
                final.add(tuple(s))
                return

            helper(i+1, s+[nums[i]])
            helper(i+1, s)
            
        helper(0, [])
        return list(final)


nums = [1,2,3]
print(Solution().subsets(nums))
