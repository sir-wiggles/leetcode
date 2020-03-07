from collections import Counter
from itertools import product

class Solution:
    def nextClosestTime(self, time: str) -> str:
        parts = time.split(':')
        cur = 60 * int(parts[0]) + int(parts[1])
        allowed = {int(x) for x in time if x != ':'}
        while True:
            cur = (cur + 1) % (24 * 60)
            if all(digit in allowed
                    for block in divmod(cur, 60)
                    for digit in divmod(block, 10)):
                return "{:02d}:{:02d}".format(*divmod(cur, 60))





print(Solution().nextClosestTime("19:34"))
print(Solution().nextClosestTime("23:59"))
print(Solution().nextClosestTime("1:23"))
print(Solution().nextClosestTime("1:2"))
print(Solution().nextClosestTime("11:2"))
print(Solution().nextClosestTime("23:59"))
    
