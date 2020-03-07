class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        bulls = 0
        matches = [0] * 10
        for (s, g) in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                matches[int(s)] += 1
                matches[int(g)] -= 1
            print(s, g, matches)
        return '{}A{}B'.format(bulls, len(secret) - bulls - sum((c for c in matches if c > 0)))

secret = "2141"
guess  = "2314"
print(Solution().getHint(secret, guess))
