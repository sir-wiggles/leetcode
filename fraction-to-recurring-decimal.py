from collections import OrderedDict

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        s = ''
        if numerator < 0 and denominator < 0:
            s = ''
        elif denominator < 0 or numerator < 0:
            s = '-'


        numerator = abs(numerator)
        denominator = abs(denominator)

        remainder = numerator % denominator
        w = numerator // denominator
        if remainder == 0:
            return f'{s}{w}'

        loc = {}
        digits = []
        i = 0
        while remainder:
            if remainder in loc:
                digits.insert(loc[remainder], '(')
                digits.append(')')
                break
            loc[remainder] = i
            remainder *= 10
            digits.append(str(remainder // denominator))
            remainder %= denominator
            i += 1
        f = ''.join(digits)
        return f'{s}{w}.{f}'

cases = [
    [1, 2],
    [3, 4],
    [1, 12],
    [1, 120],
    [2, 1],
    [8, 2],
    [2, 3],
    [1, 7],
    [4, 33],
    [4, 333],
    [4, 3333],
    [-1, 7],
    [1, -7],
    [-1, -7],
    [1, 33],
    [1, 333],
    [1, 3333],
]
for case in cases:
    print(case, Solution().fractionToDecimal(*case))

