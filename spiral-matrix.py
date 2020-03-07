import pudb
class Solution:
    def spiralOrder(self, matrix):

        n = 0
        s = len(matrix)
        if s == 0:
            return []
        e = len(matrix[0])
        w = 0
        size = s * e

        result = []

        r = 0
        c = 0
        while len(result) <= size:
            n += 1

            # >
            while c < e:
                result.append(matrix[r][c])
                c += 1
            if len(result) >= size: break

            c -= 1
            r += 1
            e -= 1

            # v
            while r < s:
                result.append(matrix[r][c])
                r += 1
            if len(result) >= size: break

            c -= 1
            r -= 1
            s -= 1

            # <
            while c >= w:
                result.append(matrix[r][c])
                c -= 1
            if len(result) >= size: break

            c += 1
            r -= 1
            w += 1

            # ^
            while r >= n:
                result.append(matrix[r][c])
                r -= 1
            if len(result) >= size: break

            c += 1
            r += 1

        return result


m = [
]

print(Solution().spiralOrder(m))
