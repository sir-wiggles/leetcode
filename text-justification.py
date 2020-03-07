from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, temp, letters = [], [], 0
        for w in words:
            # + len(temp) == spaces between words
            if letters + len(w) + len(temp) > maxWidth:
                for i in range(maxWidth - letters):
                    # if temp has only 1 word then it'll only ever be 1
                    temp[i % (len(temp) - 1 or 1)] += ' '
                res.append(''.join(temp))
                temp, letters = [], 0
            temp.append(w)
            letters += len(w)
        res.append(' '.join(temp).ljust(maxWidth))
        return res

#                        1
#         1234 5  67 8  90 1  23456
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 25

#  words = ["What","must","be","acknowledgment","shall","be"]
#  maxWidth = 16

#  words = ["Science","is","what","we","understand","well","enough","to","explain",
         #  "to","a","computer.","Art","is","everything","else","we","do"]
#  maxWidth = 20

#  words = ["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"]
#  maxWidth = 16

res = Solution().fullJustify(words, maxWidth)
print(res)
for r in res:
    print(repr(r))

