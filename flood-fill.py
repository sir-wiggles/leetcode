from typing import List
from queue import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        stack = deque([(sr, sc)])
        seen = set()

        oldColor = image[sr][sc]
        maxr = len(image)
        maxc = len(image[0])

        while stack:
            node = stack.pop()

            r, c = node
            image[r][c] = newColor
            for test in [(r-1, c), (r+1, c), (r, c+1), (r, c-1)]:
                tr, tc = test
                if tr < 0 or tr >= maxr or tc < 0 or tc >= maxc or test in seen or image[tr][tc] != oldColor:
                    continue
                stack.append(test)
                seen.add(test)
        return image

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
print(Solution().floodFill(image, sr, sc, newColor))
