from typing import List

from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0 and numCourses >= 0:
            return True

        
        al = defaultdict(set)
        for c, p in prerequisites:
            al[c].add(p)

        queue = deque()
        queue.append((prerequisites[0][0], 1))
        seen = set()

        while queue:
            node, count = queue.popleft()
            if count == numCourses:
                return True
            if node in seen:
                continue
            seen.add(node)

            for n in al[node]:
                if node in al[n]:
                    continue
                queue.append((n, count+1))
                
        return False



import unittest

class Test(unittest.TestCase):

    def test1(self):
        i = [[1, 0]]
        n = 2
        self.assertEqual(Solution().canFinish(n, i), True)

    def test2(self):
        i = [[1,0],[0,1]]
        n = 2
        self.assertEqual(Solution().canFinish(n, i), False)

    def test3(self):
        i = [
            [1,0],
            [2,3],
            [3,2],
            [0,4]
        ]
        n = 3
        self.assertEqual(Solution().canFinish(n, i), True)

    def test4(self):
        i = [
            [1,0],
            [2,3],
            [3,2],
            [0,4]
        ]
        n = 4
        self.assertEqual(Solution().canFinish(n, i), False)

    def test5(self):
        i = []
        n = 1
        self.assertEqual(Solution().canFinish(n, i), True)

    def test6(self):
        i = []
        n = 0
        self.assertEqual(Solution().canFinish(n, i), True)

    def test7(self):
        i = []
        n = 2
        self.assertEqual(Solution().canFinish(n, i), True)

    def test8(self):
        n = 3
        i = [[1,0]]
        self.assertEqual(Solution().canFinish(n, i), False)

unittest.main(exit=False)
