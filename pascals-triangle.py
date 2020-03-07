import math

class Solution:
    def generate(self, numRows):
        result = []
        for i in range(0, numRows):
            row = []
            for j in range(i+1):
                coeff = math.factorial(i) / (math.factorial(j) * math.factorial(i - j))
                row.append(coeff)
            result.append(row)
        return result



print(Solution().generate(5))
