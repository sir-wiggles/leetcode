
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        i, res = 0, 1
        for c in target:
            i = source.find(c, i)
            if i == -1:
                res += 1
                i = source.find(c)
                if i == -1:
                    return -1
            i += 1
        return res


s = 'abc'
t = 'abcbc'

s = "xyz"
t = "xzyxz"
print(Solution().shortestWay(s, t))
