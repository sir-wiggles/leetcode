from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        m = {0: 1}
        sum = 0
        for n in nums:
            sum += n
            if (sum-k) in m:
                count += m[sum-k]
            m[sum] = m.get(sum,  0) + 1
        return count



cases = [
    [[1, 1, 1], 3],
    [[1, 1, 1], 2],
    [[1, 1, 1, 1], 2],
    [[1, 1, 1], 1],
    [[1, 2, 3], 3],
    [[1], 0],
    [[-1,-1,1], 0],
    [[-1,-1,1], -1],
    [[-1,-1,1], 1]
]

for case in cases:
    print(Solution().subarraySum(*case))
