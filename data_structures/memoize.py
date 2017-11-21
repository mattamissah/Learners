
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

memo = {}
def mfib(n):
    if n in memo:
        return memo[n]
    if n == 0:
        memo[0] = 0
    if n == 1:
        memo[1] = 1
        return 1
    val = fib(n-1) + fib(n-2)
    memo[n] = val
    return val