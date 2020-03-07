from typing import List
from functools import lru_cache

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        #  mem = {}
        #  @lru_cache
        #  def r(n, c, A, B):
            #  if n == len(costs) and A == B:
                #  return c
            #  elif n == len(costs) and A != B:
                #  return float('inf')

            #  value = c + min(
                #  r(n+1, costs[n][0], A+1, B),
                #  r(n+1, costs[n][1], A, B+1)
            #  )
            #  return value

        costs.sort(key = lambda x : x[0] - x[1])
        
        total = 0
        n = len(costs) // 2
        for i in range(n):
            total += costs[i][0] + costs[i + n][1]
        return total




i = [
    [10,20],[30,200],[400,50],[30,20],
]
#  i = [
    #  [259,770],[448,54],[926,667],[184,139],[840,118],[577,469]
#  ]
i = [[174,934],[931,281],[640,326],[402,333],[426,247],[63,579],[38,362],[694,545],[767,909],[940,445],[63,451],[133,555],[898,640],[967,738],[441,293],[36,144],[201,50],[204,154],[681,871],[352,133],[359,186],[432,448],[996,876],[22,559],[907,924],[657,346],[718,746],[627,971],[497,949],[796,516],[149,254],[292,671],[543,171],[444,516],[998,717],[542,998],[80,722],[657,158],[165,443],[670,215],[659,167],[989,568],[41,303],[665,685],[708,544],[1000,878],[332,820],[604,655]]

print(Solution().twoCitySchedCost(i))
