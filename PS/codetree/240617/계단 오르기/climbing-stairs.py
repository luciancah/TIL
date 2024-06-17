n = int(input())

# f(0) = 0
# f(1) = 0
# f(2) = 1
# f(3) = 1

# 점화식: f(n) = f(n-2) + f(n-3)

dp = [0] * 1001
dp[0] = 0
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, n+1):
    dp[i] = dp[i-2] + dp[i-3]

print(dp[n] % 10007)