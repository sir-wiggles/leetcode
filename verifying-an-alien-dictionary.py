from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = {k: i for i, k in enumerate(order)}
        
        if len(words) <= 1:
            return True

        for p, word in enumerate(words[1:]):
            smallest = min(word, words[p], key=len)
            i = 0
            yes = False
            while i < len(smallest):
                if mapping[words[p][i]] < mapping[word[i]]:
                    yes = True
                    break
                elif mapping[words[p][i]] == mapping[word[i]]:
                    i += 1
                else:
                    return False
            if not yes and len(words[p]) > len(word):
                return False
        return True


words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(Solution().isAlienSorted(words, order))

words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"
print(Solution().isAlienSorted(words, order))

words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"
print(Solution().isAlienSorted(words, order))

words = ["kuvp","q"]
order = "ngxlkthsjuoqcpavbfdermiywz"
print(Solution().isAlienSorted(words, order))
