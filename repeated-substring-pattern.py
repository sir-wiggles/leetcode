from collections import defaultdict

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (2*s)[1:-1]
    
print(Solution().repeatedSubstringPattern('abcabc'))
print(Solution().repeatedSubstringPattern('ab'))
print(Solution().repeatedSubstringPattern('a'))
print(Solution().repeatedSubstringPattern('aabbaabb'))

