
class Solution:
    def minSubArrayLen(self, s, nums):

        i = 0
        j = 0
        total = 0
        ans = float('inf')

        for i in range(len(nums)):
            total += nums[i]
            while total >= s:
                ans = min(i - j + 1, ans)
                total -= nums[j]
                j += 1
        if ans == float('inf'):
            return 0
        return ans

print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 2]))
