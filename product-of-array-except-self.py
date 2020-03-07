from typing import List
from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ll = [1]
        rr = [1]
        for i, (l, r) in enumerate(zip(nums, nums[::-1])):
            ll.append(ll[i] * l)
            rr.append(rr[i] * r)

        new = []
        for l, r in zip(ll[:-1], rr[:-1][::-1]):
            new.append(l * r)
        return new





cases = [
    [1, 2, 3, 4],
]
for case in cases:
    print(Solution().productExceptSelf(case))

