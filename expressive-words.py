from typing import List
from collections import Counter

class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:

        approved = set(S)
        res = []
        for word in words:
            charSet = set(word)
            diff = len(charSet & approved)
            if diff != len(charSet) or diff != len(approved):
                continue
            elif len(word) > len(S):
                continue

            h, i = 0, 0
            j, k = 0, 0
            valid = True
            while k < len(word) and i < len(S):

                while i < len(S) and S[h] == S[i]:
                    i += 1

                while k < len(word) and word[j] == word[k]:
                    k += 1

                Wc = k - j
                Sc = i - h
                if Wc == Sc == 1:
                    pass
                elif Wc == 1 and Sc >= 3:
                    pass
                elif Wc >= 2 and Sc >= 2:
                    pass
                else:
                    valid = False
                
                h, j = i, k
            if valid:
                res.append(word)
        return len(res)





S = "heeellooo"
words = ["hello", "hi", "helo"]

S = "abcd"
words = ["abc"]

S = "abccc"
words = ["abcc"]

S = "aaa"
words = ["aaaa"]
print(Solution().expressiveWords(S, words))

