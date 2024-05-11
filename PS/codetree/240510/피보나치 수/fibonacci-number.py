n = int(input())

memo = [0] * (n + 1)

def pick_fib(n):
    if n <= 2:
        memo[n] = 1
        return 1
    if memo[n]:
        return memo[n]
    else:
        memo[n] = pick_fib(n - 1) + pick_fib(n - 2)
    return memo[n]

dp = [0] * (n + 2)
dp[1] = 1
dp[2] = 1

def pick_fib_tab(n):
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[n])

pick_fib_tab(n)