from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k < 0 or t < 0:
            return False

        def bucket(n, w):
            if n < 0:
                return (n + 1) // w
            return n//w + 1

        buckets = {}
        w = t + 1
        #  import pudb; pudb.set_trace()
        for i, n in enumerate(nums):
            b = bucket(n, w)

            if b in buckets:
                return True

            if (b-1) in buckets and abs(n - buckets[b-1]) < w:
                return True
            if (b+1) in buckets and abs(n - buckets[b+1]) < w:
                return True

            buckets[b] = n
            if i >= k:
                buckets.pop(bucket(nums[i-k], w))
        return False



nums = [1,2,3,1]
k = 3
t = 0


# Bucket [n-k <= n <= n+k]

#  w == k * 2
#  n    w    bucket
#  1 // 4 == 0
#  5 // 4 == 1
#  9 // 4 == 2
#  1 // 4 == 0 => i - j <= t !
#  5 // 4 == 1 => i - j <= t !
#  9 // 4 == 2 => 5 - 2 <= 3 !

#  nums = [1,5,9,1,5,9]
#  k = 2
#  t = 3

#  nums = [-1, -2]
#  k = 1
#  t = 1

#  nums = [-1, -1]
#  k = 1
#  t = -1

#  nums = [-1,2147483647]
#  k = 1
#  t = 2147483647

print(Solution().containsNearbyAlmostDuplicate(nums, k, t))
