n = int(input())
prices = [0] + list(map(int, input().split()))
dp = [-1 for _ in range(n+1)]
dp[0] = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        if j <= i:
            dp[i] = max(dp[i], dp[i-j] + prices[j])

print(dp[-1])