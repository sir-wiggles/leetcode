from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maximum = -1
        i = len(arr) - 1
        while i >= 0:
            if arr[i] > maximum:
                maximum, arr[i] = arr[i], maximum
            else:
                arr[i] = maximum
            i -= 1
        return arr




arr = [17,18,5,4,6,1]
arr = [56903,18666,60499,57517,26961]

      #  [60499,60499,57517,26961,-1]
print(Solution().replaceElements(arr))

