from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s = Counter(s)
        t = Counter(t)

        for k, v in t.items():
            s[k] -= v
            if s[k] < 0:
                return False
        return True

        

s = "anagram"
t = "nagaramz"
print(Solution().isAnagram(s, t))
