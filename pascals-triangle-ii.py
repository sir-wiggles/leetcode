import math
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        row = []
        for i in range( rowIndex + 1):
            row.append(int(math.factorial(rowIndex) / (math.factorial(abs(rowIndex - i)) * math.factorial(i))))
        return row


print(Solution().getRow(5))
