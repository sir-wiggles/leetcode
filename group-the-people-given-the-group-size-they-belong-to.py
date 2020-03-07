from typing import List
from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        output = defaultdict(list)
        for id, size in enumerate(groupSizes):
            output[size].append(id)

        final = []
        for k, v in output.items():
            temp = []
            for i in v:
                if len(temp) < k:
                    temp.append(i)
                else:
                    final.append(temp)
                    temp = [i]
            if len(temp) == k:
                final.append(temp)
        return final





groupSizes = [3,3,3,3,3,1]
#  groupSizes = [1, 2, 1, 2]

print(Solution().groupThePeople(groupSizes))
