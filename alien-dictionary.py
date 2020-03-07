from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:

        order = []
        largest = max(words, key=lambda x: len(x))
        seen = set()
        for i in range(len(largest)):
            for word in words:
                if i >= len(word):
                    continue
                for c in word[i:i+1]:
                    if c in seen:
                        continue
                    order.append(c)
                    seen.add(c)

        return order

words = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

'imsrukbqytexoljdwhfczpavng'
 i    kb  t  o         a
   sehfnd
words = ['is', 'kind', 'best', 'test', 'the', 'this', 'of', 'a']

print(Solution().alienOrder(words))
