import pudb

class Solution:
    def strStr(self, haystack, needle):

        pudb.set_trace()
        needleLen = len(needle)
        if needleLen == 0:
            return 0

        for i, letter in enumerate(haystack):
            if letter == needle[0] and haystack[i:i+needleLen] == needle:
                return i
        return -1


print(Solution().strStr('hello', 'll'))
