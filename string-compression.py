from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 0:
            return 0

        c, i, j = 0, 0, 0
        while j < len(chars):
            if chars[i] == chars[j]:
                j += 1
                c += 1
            elif c == 1:
                i += 1
                chars[i] = chars[j]
                c = 0
            elif c > 1:
                chars[i] = chars[i] + str(c)
                i += 1
                chars[i] = chars[j]
                c = 0

        if c == 1:
            chars[i] = chars[i] 
        else:
            chars[i] = chars[i] + str(c)
        i += 1
        size = sum([len(x) for x in chars[:i]])
        chars[:] = list(''.join(chars[:i]))
        return size


i = list('aabbcccccccccc')
print(Solution().compress(i))
print(i)
