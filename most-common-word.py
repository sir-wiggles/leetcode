from typing import List
from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        paragraph = re.sub("[!?',;.]", " ", paragraph).lower().split()
        banned = set(banned)
        m = float('-inf')
        word = ''
        for k, v in Counter(paragraph).items():
            if k not in banned and v > m:
                m = v
                word = k
        return word




p = "Bob hit a ball?, the hit BALL' flew far after it was hit."
b = ["hit"]

p = "a, a, a, a, b,b,b,c, c"
b = ["a"]
print(Solution().mostCommonWord(p, b))
