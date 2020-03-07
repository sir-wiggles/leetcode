from typing import List
from functools import lru_cache

class Solution:

    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 0:
            return 0
        colors = set(range(len(costs[0])))

        @lru_cache()
        def r(index, cc):
            total = costs[index][cc]
            if index == len(costs)-1:
                return total
            c1, c2 = colors.difference(set([cc]))
            total += min(
                r(index+1, c1),
                r(index+1, c2)
            )
            return total
        return min( r(0, cc) for cc in colors )


#  i = [ [17,2,17], [16,16,5], [14,3,19] ] 
#  i = [ [3,5,3], [6,17,6], [7,13,18], [9,10,18] ]
i = [[4,20,19],[12,12,19],[10,11,20],[1,7,20],[4,20,1],[7,19,17],[4,18,16],[16,6,10],[5,2,4],[9,8,5],[13,18,15],[12,10,14],[11,16,3],[13,1,14],[13,4,6],[17,1,10],[7,3,16],[20,7,3],[3,9,19],[17,17,14],[14,1,14]]

#  i = [[20,18,4],[9,9,10]]

#  i = [[7,6,2]]
print(Solution().minCost(i))
