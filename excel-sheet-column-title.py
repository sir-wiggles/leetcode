from string import ascii_uppercase

class Solution:
    def convertToTitle(self, n: int) -> str:
        n -= 1
        header = []
        while n >= 0:
            print('.')
            header.append(ascii_uppercase[n % 26])
            n = (n // 26) - 1
        return ''.join(header[::-1])


print(Solution().convertToTitle(26))
print(Solution().convertToTitle(27))
print(Solution().convertToTitle(52))
print(Solution().convertToTitle(53))
print(Solution().convertToTitle(701))
print(Solution().convertToTitle(702))
print(Solution().convertToTitle(703))
print(Solution().convertToTitle(26**4 + 26**3 + 26**2 + 25))
print(Solution().convertToTitle(26**4 + 26**3 + 26**2 + 26))
print(Solution().convertToTitle(26**4 + 26**3 + 26**2 + 26 + 2))
