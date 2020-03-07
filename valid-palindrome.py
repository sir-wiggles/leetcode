from string import ascii_lowercase, digits

class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = set(ascii_lowercase + digits) 
        new = []
        for c in s.lower():
            if c in letters:
                new.append(c)

        return ''.join(new) == ''.join(new[::-1])

s = "A man, a plan, a canal: Panama"
s = "race a car"
s = '0P'
print(Solution().isPalindrome(s))
