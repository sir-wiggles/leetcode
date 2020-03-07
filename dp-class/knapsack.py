#  Given two integer arrays to represent weights and profits of ‘N’ items, we
#  need to find a subset of these items which will give us maximum profit such
#  that their cumulative weight is not more than a given number ‘C’. Each item
#  can only be selected once, which means either we put an item in the knapsack
#  or we skip it.


class Solution_BF:
    '''
    Brute-force solution
    '''
    def knapsack(self, profits, weights, capacity, currentIndex=0):

        if capacity <= 0 or currentIndex >= len(profits):
            return 0

        p1 = 0
        if weights[currentIndex] <= capacity:
            p1 = profits[currentIndex] + self.knapsack(
                profits,
                weights,
                capacity - weights[currentIndex],
                currentIndex + 1
            )

        p2 = self.knapsack(profits, weights, capacity, currentIndex + 1)
        p = max(p1, p2)
        return p

class Solution_BFM:
    '''
    Brute-force with memoization
    time:  O(n * c)
    space: O(n * c)
    where n is number of items and c is capacity
    '''
    def __init__(self):
        self.mem = {}

    def knapsack(self, profits, weights, capacity, currentIndex=0):

        if capacity <= 0 or currentIndex >= len(profits):
            return 0

        if (currentIndex, capacity) in self.mem:
            return self.mem[(currentIndex, capacity)]

        p1 = 0
        if weights[currentIndex] <= capacity:
            p1 = profits[currentIndex] + self.knapsack(
                profits,
                weights,
                capacity - weights[currentIndex],
                currentIndex + 1
            )

        p2 = self.knapsack(profits, weights, capacity, currentIndex + 1)
        p = max(p1, p2)
        self.mem[(currentIndex, capacity)] = p
        return p

class Solution_DP_v0:
    '''
    Dynamic programming solution
    time:  O(n * c)
    space: O(n * c)
    '''

    def knapsack(self, profits, weights, capacity):
        np = len(profits)

        dp = [[0 for c in range(capacity+1)] for r in range(np+1)]

        for i in range(1, np+1):
            for c in range(1, capacity + 1):
                p1, p2 = 0, 0
                if weights[i-1] <= c:
                    p1 = profits[i-1] + dp[i-1][c-weights[i-1]]
                p2 = dp[i-1][c]
                dp[i][c] = max(p1, p2)

        return dp[-1][-1]


class Solution_DP:
    '''
    Dynamic programming solution
    time:  O(n * c)
    space: O(c)
    '''
    def knapsack(self, profits, weights, maxCapacity):
        # weights needs to be sorted and profits needs to keep the same mapping
        # as weights
        profitsAndWeights = sorted(zip(profits, weights), key=lambda x: x[1])
        dp = [0] * (maxCapacity+1)

        for (profit, weight) in profitsAndWeights:
            for capacity in range(1, maxCapacity + 1):
                p1 = dp[capacity]
                if weight <= capacity:
                    p1 = profit + dp[capacity-weight]
                p2 = dp[capacity-1]
                dp[capacity] = max(p1, p2)
        return dp[-1]

#  print(Solution_BF().knapsack(   [1, 6, 10, 16, 20], [1, 2, 3, 5, 4], 9))
#  print(Solution_BFM().knapsack(  [1, 6, 10, 16, 20], [1, 2, 3, 5, 4], 9))
#  print(Solution_DP_v0().knapsack([1, 6, 10, 16, 20], [1, 2, 3, 5, 4], 9))
print(Solution_DP_v0().knapsack([1, 6, 10, 20, 16], [1, 2, 3, 5, 4], 9))
print(Solution_DP().knapsack(   [1, 6, 10, 20, 16], [1, 2, 3, 5, 4], 9))

