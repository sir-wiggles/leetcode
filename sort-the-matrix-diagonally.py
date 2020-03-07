from typing import List
from functools import lru_cache

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        numbers = sorted([n for row in mat for n in row])

        r = 0
        c = 0
        i = 0
        import pudb; pudb.set_trace()
        while r < len(mat) or c < len(mat[0]):
            # horizontal
            if r < len(mat):
                for cc in range(r, len(mat[0])):
                    mat[r][cc] = numbers[i]
                    i += 1

            # vert
            if c < len(mat[0]):
                for rr in range(c, len(mat)):
                    mat[rr][c] = numbers[i]
                    i += 1

            r += 1
            c += 1

        return mat



mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
for r in Solution().diagonalSort(mat):
    print(r)
