

m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]



def work(m):
        cols = len(m[0])
        rows = len(m)

        def getDiagonal(r, c, reverse=False):
            temp = []
            while c >= 0 and r < rows:
                temp.append(m[r][c])
                r += 1
                c -= 1
            if reverse:
                temp.reverse()

            return temp

        size = rows + cols

        result = []

        start = [0, -1]
        for i in range(size):
            if i >= cols:
                start[0] = i - cols + 1
            else:
                start[1] = i

            result.extend(getDiagonal(*start, reverse=(i+1)%2))
        return result

print(work(m))
