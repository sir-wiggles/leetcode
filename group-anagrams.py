from typing import List
from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anag = defaultdict(list)
        for word in strs:
            key = tuple(sorted(Counter(word).items()))
            anag[key].append(word)

        res = []
        for _, v in anag.items():
            res.append(v)
        return res

test = ["kit","all","gen","bmw","cog","ids","sis","gog","awe","hen","fez","les","ten","sow","mac","ark","bmw","fdr","liz","wee","nth","gob","bar","ark","and","pan","icy","ira","ewe","kip","sun","mys","min","gay","paw","rep","lap","tex","let","mil","poe","was","poe","jay","coy","gas","pip","tog","bra","wok","sag","pay","fox","sui","ben","saw","dog","mat","jig"]
print(Solution().groupAnagrams(test))
