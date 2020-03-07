
class Solution:
    def twoSum(self, numbers, target):
        m = {}
        for i, number in enumerate(numbers):
            m[target-number] = i + 1

        for i, number in enumerate(numbers):
            if number in m:
                return [i + 1, m[number]]


print(Solution().twoSum([2, 7 , 11, 15], 9))
