class Solution:
    def removeDuplicates(self, nums):

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        i = 0
        j = 1
        while j < len(nums):
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            i += 1
            if j >= len(nums):
                break
            nums[i] = nums[j]
        return i


print(Solution().removeDuplicates([0]))
