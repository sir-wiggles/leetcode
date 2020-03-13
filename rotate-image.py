from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        maxr = len(matrix)
        for i in range(maxr):
            for j in range(i, maxr):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            matrix[i][:] = matrix[i][::-1]
            
i = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

Solution().rotate(i)
for r in i:
    print(r)
