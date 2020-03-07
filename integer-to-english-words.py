
class Solution:

    def __init__(self):
        self.to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
                'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split(' ')
        self.tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

    def numberToWords(self, n):

        def words(n):
            if n == 0:
                return []
            if n < 20:
                return [self.to19[n-1]]
            if n < 100:
                return [self.tens[n//10-2]] + words(n%10)
            if n < 1000:
                return [self.to19[n//100-1]] + ['Hundred'] + words(n%100)
            else:
                for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
                    if n < 1000 ** (p+1):
                        return words(n//1000**p) + [w] + words(n%1000**p)
        return ' '.join(words(n)) or 'Zero'


for n in [0, 1, 10, 19, 20, 99, 100, 101, 115, 999, 1000, 1001, 15000, 100000, 1000000, 1000000000, 123456789, 12345678905]:
    print(n, Solution().numberToWords(n))

