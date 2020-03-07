from collections import defaultdict
from typing import List

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

        res = []

        words = [self.f(w) for w in words]

        for query in queries:
            qs = self.f(query)
            count = 0
            for word in words:
                if qs < word:
                    count += 1
            res.append(count)
        return res

    def f(self, w: str):
        m = defaultdict(int)
        for l in w:
            m[l] += 1

        char = sorted(m.keys())[0]
        return m[char]





queries = ["bbb","cc"]
words = ["a","aa","aaa","aaaa"]

print(Solution().numSmallerByFrequency(queries, words))
#  print(Solution().f('zaaaz'))
