from typing import List
from collections import defaultdict

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:

        w1, w2, m = -1, -1, float('inf')
        for i, word in enumerate(words):
            if word1 == word:
                w1 = i
            elif word2 == word:
                w2 = i
            if w1 != -1 and w2 != -1:
                m = min(abs(w1 - w2), m)
        return m

words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"
print(Solution().shortestDistance(words, word1, word2))
