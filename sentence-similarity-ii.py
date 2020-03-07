from typing import List
from collections import defaultdict, deque

class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:

        if len(words1) != len(words2):
            return False

        al = defaultdict(set)
        for k, v in pairs:
            al[k].add(v)
            al[v].add(k)

        def search(w1, w2):

            seen = set()
            queue = deque([w1])
            while queue:
                node = queue.popleft()
                if node == w2:
                    return True
                if node in seen:
                    continue
                seen.add(node)

                for n in al[node]:
                    if n == w2:
                        return True
                    queue.append(n)
            return False


        for w1, w2 in zip(words1, words2):
            if not search(w1, w2):
                return False
        return True

pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]]
words1 = ["great", "acting", "skills"] 
words2 = ["fine", "drama", "talent"]

words1 = ["an","extraordinary","meal","meal"]
words2 = ["one","good","dinner"]
pairs = [["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],["excellent","good"],["fine","good"],["nice","good"],["any","one"],["some","one"],["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],["take","have"],["fruits","meal"],["brunch","meal"],["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],["have","own"],["extremely","very"],["actually","very"],["really","very"],["super","very"]]

words1 = ["I","have","enjoyed","happy","thanksgiving","holidays"]
words2 = ["I","have","enjoyed","happy","thanksgiving","holidays"]
pairs = [["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],["excellent","good"],["fine","good"],["nice","good"],["any","one"],["some","one"],["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],["take","have"],["fruits","meal"],["brunch","meal"],["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],["have","own"],["extremely","very"],["actually","very"],["really","very"],["super","very"]]
print(Solution().areSentencesSimilarTwo(words1, words2, pairs))
