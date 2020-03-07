from typing import List
from collections import defaultdict

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:

        a = defaultdict(set)
        for i, v in enumerate(A):
            a[v].add(i)

        b = defaultdict(set)
        for i, v in enumerate(B):
            b[v].add(i)

        dominos = len(A)
        minimum = float('inf')

        for i, ai in a.items():
            bi = b[i]
            if len(ai.union(bi)) == dominos:
                if len(bi) < minimum:
                    minimum = min(len(ai.difference(bi)), len(bi.difference(ai)))

        if minimum == float('inf'):
            return -1
        return minimum


A = [2,1,2,4,2,2]
B = [5,2,6,2,3,2]
print(Solution().minDominoRotations(A, B))
