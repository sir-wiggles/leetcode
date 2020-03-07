from typing import List

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        items.sort(key = lambda x: (x[0], -x[1]))
        nscores = 5

        res = []
        i = 0
        current_sid = items[0][0]
        items.append([-float('inf'), 0])
        while i < len(items) and current_sid != -float('inf'):
            res.append([current_sid, sum(map(lambda x: x[1], items[i:i+nscores]))//nscores])
            i += nscores
            while i < len(items) and items[i][0] == current_sid:
                i += 1
            current_sid = items[i][0]
        return res



i = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
print(Solution().highFive(i))

