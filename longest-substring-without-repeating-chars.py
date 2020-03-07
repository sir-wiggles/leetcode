class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        i, j = 0, 1
        longest = 0
        while j < len(s):
            seen = set(s[i])
            while j < len(s) and s[j] not in seen:
                seen.add(s[j])
                j += 1
            if j - i > longest:
                longest = j - i
            i += 1
            j = i + 1
        return longest

print(Solution().lengthOfLongestSubstring('abcabcb'))
