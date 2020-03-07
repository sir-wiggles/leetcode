from collections import defaultdict

class Solution:
    def countLetters(self, S: str) -> int:
        counter = defaultdict(int)

        def updateCounter(i, j):
            key = S[i]
            for p, c in enumerate(S[i:j]):
                counter[key] += (j-i-p)
                key += c
            return j, j+1 

        i, j = 0, 1
        while j < len(S):
            if S[i] == S[j]:
                j += 1
                continue
            else:
                i, j = updateCounter(i, j)
        else:
            i, j = updateCounter(i, j)
        return sum([value for value in counter.values()])



s = "aaaba"
#  s = "aaaaaaaaaa"
print(Solution().countLetters(s))
