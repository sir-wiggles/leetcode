from typing import List
from functools import lru_cache

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answers = set()

        def recursive(count, sum, i, parts):
            if count > 4:
                return
            if count == 4 and sum == target:
                answers.add(parts)
            if i >= len(nums):
                return

            recursive(count + 1, sum + nums[i], i+1, parts | 1<<i)
            recursive(count, sum, i+1, parts)

        recursive(0, 0, 0, 1<<len(nums))

        final = set()
        for answer in answers:
            count = 0
            i = 0
            temp = []
            while count < 4:
                if (answer >> i) & 1:
                    temp.append(nums[i])
                    count += 1
                i+=1 
            temp.sort()
            final.add(tuple(temp))
        return final

        

nums = [1, 0, -1, 0, -2, 2, 3, 4, 5, 6, 7, 8, 9, -9, -8, -7]
target = 0

nums = [-5,5,4,-3,0,0,4,-2]
target = 4

nums = [-500,-481,-480,-469,-437,-423,-408,-403,-397,-381,-379,-377,-353,-347,-337,-327,-313,-307,-299,-278,-265,-258,-235,-227,-225,-193,-192,-177,-176,-173,-170,-164,-162,-157,-147,-118,-115,-83,-64,-46,-36,-35,-11,0,0,33,40,51,54,74,93,101,104,105,112,112,116,129,133,146,152,157,158,166,177,183,186,220,263,273,320,328,332,356,357,363,372,397,399,420,422,429,433,451,464,484,485,498,499]
target = 2139

for row in Solution().fourSum(nums, target):
    print(row)
