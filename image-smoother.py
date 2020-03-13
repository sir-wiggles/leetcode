from itertools import product

class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:

        maxr = len(M)
        maxc = len(M[0])
        
        def surrounding(r, c):
            if  r == 0 and c == 0:
                return sum([M[r][c], M[r+1][c], M[r+1][c+1], M[r][c+1]]) // 4
            elif r == 0 and c == maxc-1:
                return sum([M[r][c], M[r+1][c], M[r+1][c-1], M[r][c-1]]) // 4
            elif r == maxr-1 and c == 0:
                return sum([M[r][c], M[r-1][c], M[r-1][c+1], M[r][c+1]]) // 4
            elif r == maxr-1 and c == maxc-1:
                return sum([M[r][c], M[r-1][c], M[r-1][c-1], M[r][c-1]]) // 4
                
            elif r == 0:
                return sum([M[r][c], M[r][c-1], M[r][c+1], M[r+1][c-1], M[r+1][c], M[r+1][c+1]]) // 6
            elif r == maxr-1:
                return sum([M[r][c], M[r][c-1], M[r][c+1], M[r-1][c-1], M[r-1][c], M[r-1][c+1]]) // 6
            elif c == 0:
                return sum([M[r-1][c], M[r][c], M[r+1][c], M[r-1][c+1], M[r][c+1], M[r+1][c+1]]) // 6
            elif c == maxc-1:
                return sum([M[r-1][c], M[r][c], M[r+1][c], M[r-1][c-1], M[r][c-1], M[r+1][c-1]]) // 6
            
            else:
                cells = []
                for _r in range(r-1, r+2):
                    for _c in range(c-1, c+2):
                        cells.append(M[_r][_c])
                return sum(cells) // len(cells)
        
        copy = [[0] * maxc for _ in range(maxr)]
        for row in M:
            row.insert(0, 0)
            row.append(0)
        M = ([0] * maxc) + M + ([0] * maxc)

        ranges = [range(maxr), range(maxc)]
        for r, c in product(*ranges):
            r += 1
            c += 1
            copy[r-1][c-1] = surrounding(r, c)
        return copy
