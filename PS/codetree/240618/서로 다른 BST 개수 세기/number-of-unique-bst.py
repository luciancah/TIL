n = int(input())
dp = [0] * 21

memo = [-1 for _ in range(n+1)]

def dp(n):
    if memo[n] != -1:
        return memo[n]

    if n <= 1:
        return 1
    
    ans = 0
    for i in range(n):
        ans += dp(i) * dp(n-i-1)

    memo[n] = ans
    return memo[n]

print(dp(n))