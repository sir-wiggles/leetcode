
def Fib1(n):
    if n < 2:
        return n
    return Fib1(n - 2) + Fib1(n - 1)

def Fib2(n):

    mem = [-1] * (n+1)

    def fib(n):
        if n < 2:
            return n
        if mem[n] >= 0:
            return mem[n]
        mem[n] = fib(n-1) + fib(n-2)
        return mem[n]

    return fib(n)

def Fib3(n):
    dp = [0, 1]

    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]

for x in range(10):
    print(x, Fib3(x))
