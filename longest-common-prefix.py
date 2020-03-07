class Solution:
    def longestCommonPrefix(self, strs):

        if len(strs) == 0:
            return ""

        prefix = ""
        end = False
        for i in range(min(map(len, strs))):
            for word in strs:
                if word[i] != strs[0][i]:
                    end = True
                    break
            if end:
                break
            prefix += strs[0][i]
        return prefix


print(Solution().longestCommonPrefix(['flower', 'flow', 'flight']))
