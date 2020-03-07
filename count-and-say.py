class Solution:
    def countAndSay(self, n: int) -> str:
        base = ['1']
        if n == 1:
            return '1'

        new = []
        for n in range(1, n):
            new = []
            c, i, j = 0, 0, 0
            while j < len(base):
                if base[i] == base[j]:
                    c += 1
                else:
                    new.extend([str(c), base[i]])
                    i = j
                    c = 0
                    j -= 1
                j += 1

            new.extend([str(c), base[i]])
            base = new[:]

        return ''.join(new)
            



#  1.     1
#  2.     11
#  3.     21
#  4.     1211
#  5.     111221
#  6.     312211

n = 20
print(Solution().countAndSay(n))
