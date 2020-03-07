class Solution:
    def findMaxConsecutiveOnes(self, nums):
        j = 0
        i = 0
        longest = 0
        while i < len(nums):
            if nums[i] == 1:
                j = i
                while j < len(nums) and nums[j] == 1:
                    j += 1
                if j - i > longest:
                    longest = j - i
                i = j
            i += 1
        return longest


print(Solution().findMaxConsecutiveOnes([0]))
print(Solution().findMaxConsecutiveOnes([1]))
print(Solution().findMaxConsecutiveOnes([0, 1]))
print(Solution().findMaxConsecutiveOnes([1, 0]))
print(Solution().findMaxConsecutiveOnes([1, 1]))
print(Solution().findMaxConsecutiveOnes([0, 0]))
print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
