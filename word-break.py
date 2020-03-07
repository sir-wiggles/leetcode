from typing import List
from functools import lru_cache

class Solution:
    def wordBreak(self, word: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        @lru_cache(None)
        def split(start):
            if start == len(word):
                return True
            for end in range(start+1, len(word)+1):
                res = split(end)
                sub = word[start:end]
                if sub in words and res:
                    return True
            return False
        return split(0)



s = "applepenapple"
wordDict = ["apple", "pen"]

s = "cat"
wordDict = ["cats", "dog", "sand", "and", "cat"]

print(Solution().wordBreak(s, wordDict))
