import unittest
from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        al = defaultdict(list)
        for f, t in tickets:
            al[f].append(t)

        END = 'JFK'

        valid = []

        def search(start, path):
            if len(path) == len(tickets) + 1:
                valid.append(''.join(path))
                return

            for n in al[start]:
                search(n, path + [n])

        search(END, [END])
        valid.sort()
        return list(zip(*(iter(valid[0]), ) * 3))


class Test(unittest.TestCase):

    def setUp(self):
        self.s = Solution().findItinerary

    def test1(self):
        l = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        o = ["JFK", "MUC", "LHR", "SFO", "SJC"]
        res = self.s(l)
        self.assertListEqual(res, o)

    def test2(self):
        l = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

        o = ["JFK","ATL","JFK","SFO","ATL","SFO"]
        #  o = ["JFK","SFO","ATL","JFK","ATL","SFO"]

        res = self.s(l)
        self.assertListEqual(o, res)

unittest.main(exit=False)
