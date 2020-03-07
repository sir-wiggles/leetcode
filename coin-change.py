from typing import List
from typing import List
from functools import lru_cache

inf = float('inf')

class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:

        @lru_cache(maxsize=None)
        def z(remaining: int):
            # if the amount goes negative then this isn't valid
            if remaining < 0:
                return inf
            # we've found a valid combination
            if remaining == 0:
                return 0

            minimum = inf
            for coin in coins:
                minimum = min(z(remaining - coin) + 1, minimum)
            return minimum 

        total = z(amount)
        return total if total != inf else -1


coins = [1, 2, 5]
amount = 11

coins = [186,419,83,408]
amount = 6249

#  coins = [2]
#  amount = 3
print(Solution().coinChange(coins, amount))
