class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.r(s)

    def r(self, s, deletion=0):

        if len(s) <= 1:
            return True

        if s[0] != s[-1]:
            deletion += 1
            if deletion > 1:
                return False
            return self.r(s[:-1], deletion=deletion) or self.r(s[1:], deletion=deletion) 
        else:
            return self.r(s[1:-1], deletion=deletion)


s = ''
print(Solution().validPalindrome(s))
