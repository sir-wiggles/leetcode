from typing import List
from collections import defaultdict, deque

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        if len(transactions) == 0:
            return 0

        ledger = defaultdict(int)
        for (f, t, a) in transactions:
            ledger[f] -= a
            ledger[t] += a

        net = [v for v in ledger.values() if v != 0]

        count = 0

        print(ledger)
        print(net)
        return self.possible_solutions(0, 0, net)

    def possible_solutions(self, person_id, tx_count, debts):

        while person_id < len(debts) and debts[person_id] == 0:
            person_id += 1

        if person_id >= len(debts):
            return tx_count

        min_num_transactions_seen = float('inf')
        for i in range(person_id + 1, len(debts)):
            # Can we lower the number of transactions by "canceling out" another balance?
            if debts[i] * debts[person_id] < 0:
                debts[i] += debts[person_id]
                candidate_min = self.possible_solutions(person_id + 1, tx_count + 1, debts)
                min_num_transactions_seen = min(min_num_transactions_seen, candidate_min)
                debts[i] -= debts[person_id] # Reset the debts array to test another payment options
        return min_num_transactions_seen




#  test = [[0,1,10], [1,0,1], [1,2,5], [2,0,5]]
#  print(Solution().minTransfers(test)) == 1

#  test = [[0,1,10], [2,0,5]]
#  print(Solution().minTransfers(test))

test = [[0,1,5],[2,3,1],[2,0,1],[4,0,2]]
print(Solution().minTransfers(test))

#  test = []
#  print(Solution().minTransfers(test))

#  test = [[0,1,10]]
#  print(Solution().minTransfers(test))

#  test = [[0,1,1],[1,2,1],[2,0,1]]
#  print(Solution().minTransfers(test))

#  test = [[0,3,2],[1,4,3],[2,3,2],[2,4,2]]
#  print(Solution().minTransfers(test))

test = [[0,6,7],[0,7,7],[1,4,5],[1,5,4],[2,5,2],[3,7,1]]
print(Solution().minTransfers(test)) == 6
