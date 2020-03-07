from typing import List, Set

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxarea = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0': 
                    matrix[i][j] = 0
                    continue

                # compute the maximum width and update dp with it
                width = matrix[i][j] = int(matrix[i][j-1]) + 1 if j else 1

                # compute the maximum area rectangle with a lower right corner at [i, j]
                for k in range(i, -1, -1):
                    width = min(width, matrix[k][j])
                    maxarea = max(maxarea, width * (i-k+1))
        return maxarea




case = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

case = []
case = [["0"]]
#  case = [["1","1"]]
#  case = [
    #  ["1","0","1","0","0"],
    #  ["1","0","1","1","1"],
    #  ["1","1","1","1","1"],
    #  ["1","0","0","1","0"]
#  ]

case = [
    ["1","1","0","1"],
    ["1","1","0","1"],
    ["1","1","1","1"]
]

case = [
    ["1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","0"],
    ["1","1","1","1","1","1","1","0"],
    ["1","1","1","1","1","0","0","0"],
    ["0","1","1","1","1","0","0","0"]
]
print(Solution().maximalRectangle(case))


