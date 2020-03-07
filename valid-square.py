from typing import List
import math

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:

        a, b, c, d = sorted([p1, p2, p3, p4], key=lambda x: (x[0], x[1]))

        s1 = math.dist(a, b)
        s2 = math.dist(b, d)
        s3 = math.dist(d, c)
        s4 = math.dist(c, d) 

        d1 = math.dist(d, a)
        d2 = math.dist(b, c) 

        return s1 > 0 and s1 == s2 and s2 == s3 and s3 == s4 and d1 == d2 
    
p1 = [0,0]
p2 = [1,1]
p3 = [1,0]
p4 = [0,1]

p1 = [-2246,-6329]
p2 = [-2628,-4837]
p3 = [-754,-5947]
p4 = [-1136,-4455]



p1 = [0,0]
p2 = [5,0]
p3 = [5,4]
p4 = [0,4]

p1 = [0,0]
p2 = [0,0]
p3 = [0,0]
p4 = [0,0]
print(Solution().validSquare(p1, p2, p3, p4))
