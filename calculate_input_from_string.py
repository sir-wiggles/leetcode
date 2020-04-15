from typing import List
import operator
import re


class Calculator:
    symbols = {
        '*': operator.mul,
        '/': operator.truediv,
        '+': operator.add,
        '-': operator.sub,
    }

    def split(self, s: str) -> List[str]:
        parts = re.split('([*/+-])', s)
        return list(map(lambda x: float(x) if x.isdecimal() else x, parts))

    def eval(self, s: str) -> float:
        parts = self.split(s)
        for operators in [{'*', '/'}, {'+', '-'}]:
            index = 0
            while len(parts) > 1 and index < len(parts):
                element = parts[index]
                if element not in operators:
                    index += 1
                    continue
                new = self.symbols[element](parts[index-1], parts[index+1])
                parts = parts[:index-1] + [new] + parts[index+2:]
                index = 0

        return parts[0]


calc = Calculator()
assert calc.eval('12+1*3') == 15
assert calc.eval('12/1+3') == 15
assert calc.eval('12/1*3') == 36
assert calc.eval('1+2-3*4/6') == 1
