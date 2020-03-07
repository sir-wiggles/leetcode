class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return

        start = 0
        count = 0
        while count < len(nums):
            current = start
            prev = nums[start]
            while True:
                next = (current + k) % len(nums)
                temp = nums[next]
                nums[next] = prev
                prev = temp
                current = next
                count += 1
                if start == current:
                    break
            start += 1

test = [1, 2, 3, 4, 5, 6, 7]
Solution().rotate(test, 7)
print(test)
