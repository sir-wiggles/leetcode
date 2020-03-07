from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        maxr = len(matrix)
        if maxr == 0:
            return 0
        maxc = len(matrix[0])

        dp = [[0 for c in range(maxc+1)] for r in range(maxr+1)]

        largest = 0
        for r in range(1, maxr+1):
            for c in range(1, maxc+1):
                cell = matrix[r-1][c-1]
                if cell == '1':
                    level = min(int(dp[r-1][c-1]), int(dp[r-1][c]), int(dp[r][c-1])) + 1
                    if level > largest:
                        largest = level
                    dp[r][c] = level

        for x in dp:
            print(x)
        return largest**2

test = [
    '00000',
    '01111',
    '11111',
    '11111',
]


#  test = [
        #  ["0","0","0","1"],
        #  ["1","1","0","1"],
        #  ["1","1","1","1"],
        #  ["0","1","1","1"],
        #  ["0","1","1","1"]
        #  ]

#  test = [
    #  ['1']
#  ]

for i, r in enumerate(test):
    test[i] = list(r)

print(Solution().maximalSquare(test))
