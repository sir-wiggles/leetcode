class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        num1 = num1[::-1]
        num2 = num2[::-1]

        if len(num1) >= len(num2):
            largest = num1
            smallest = num2
        else:
            largest = num2
            smallest = num1

        res = []
        i = 0
        carry = False
        for size, number in enumerate([smallest, largest]):
            while i < len(number):
                if size == 0:
                    sum = int(largest[i]) + int(smallest[i])
                else:
                    sum = int(largest[i])

                if carry:
                    sum += 1
                    carry = False

                if sum > 9:
                    carry = True
                    res.append(sum%10)
                else:
                    res.append(sum)
                i += 1

        if carry:
            res.append(1)
        return ''.join(map(str, res))[::-1]




a = '163'
b = '456'
a = '9'
b = '99'
# 619
print(Solution().addStrings(a, b))
