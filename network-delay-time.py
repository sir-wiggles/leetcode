from typing import List
from collections import defaultdict, deque
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:

        al = defaultdict(set)
        for (u, v, t) in times:
            al[u].add((v, t))

        queue = [(0, K)]
        times = defaultdict(int)

        while queue:
            (time, node) = heapq.heappop(queue)
            if node in times:
                continue
            times[node] = time

            for (neighbor, distance) in al[node]:
                heapq.heappush(queue, (time + distance, neighbor))

        print(times)
        if len(times) == N:
            return max(times.values())
        return -1
        


times = [
    [2,1,1],
    [2,3,1],
    [3,4,1],
    #  [2,5,10],
    #  [5,6,10],
    #  [6,4,30]
]
N = 4
K = 1

#  times = [[1,2,1],[2,3,2],[1,3,4]]
#  N = 3
#  K = 1

print(Solution().networkDelayTime(times, N, K))
