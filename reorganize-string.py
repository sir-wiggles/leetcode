from collections import Counter
import heapq


class Solution:

    def reorganizeString(self, S):
        freq = sorted([(v, l) for l, v in Counter(S).items()])
        ans, N = [], len(S)
        for n, l in freq:
            if n > (N+1)//2: 
                return ""
            ans.extend(n * l)
        ans[::2], ans[1::2] = ans[N//2:], ans[:N//2]
        return "".join(ans)


    def reorganizeString_v1(self, S: str) -> str:
        if len(S) == 0:
            return S

        def check(s):
            for i, l in enumerate(s[1:]):
                if s[i] == l:
                    return ""
            return s
        
        freq = [[-v, k] for k, v in Counter(S).items()]
        heapq.heapify(freq)
        #  import pudb.b
        ans = ""
        largest = heapq.heappop(freq)
        while freq:
            current = heapq.heappop(freq)
            ans += largest[1] + current[1]
            largest[0], current[0] = largest[0] + 1, current[0] + 1
            if current[0] < 0:
                heapq.heappush(freq, current)

            if len(freq) and largest[0] == 0:
                largest = heapq.heappop(freq)
            elif len(freq) and largest[0] > freq[0][0]:
                largest = heapq.heappushpop(freq, largest)
        else:
            if largest[0] < 0:
                ans += largest[1] * -largest[0]
        return check(ans)

            
import unittest
class Test(unittest.TestCase):

    def check(self, s):
        print(s)
        if len(s) == 0:
            return False
        for i, l in enumerate(s[1:]):
            if s[i] == l:
                return False
        return True

    def test1(self):
        s = 'aab'
        self.assertEqual(self.check(Solution().reorganizeString(s)), True)

    def test2(self):
        s = 'aaab'
        self.assertEqual(self.check(Solution().reorganizeString(s)), False)

    def test3(self):
        #    12345 12 12
        s = "aaaaa bb cc"
        s = s.replace(" ", "")
        self.assertEqual(self.check(Solution().reorganizeString(s)), True)

    def test4(self):
        s = "aaabbbccc"
        s = s.replace(" ", "")
        self.assertEqual(self.check(Solution().reorganizeString(s)), True)

    def test5(self):
        s = ""
        self.assertEqual(self.check(Solution().reorganizeString(s)), False)

    def test6(self):
        s = "a"
        self.assertEqual(self.check(Solution().reorganizeString(s)), True)

    def test7(self):
        s = "aa"
        self.assertEqual(self.check(Solution().reorganizeString(s)), False)

    def test8(self):
        s = "ab"
        self.assertEqual(self.check(Solution().reorganizeString(s)), True)

unittest.main(exit=False)
        
