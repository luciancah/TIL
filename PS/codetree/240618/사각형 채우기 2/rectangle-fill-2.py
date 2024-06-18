n = int(input())
dp = [0 for _ in range(1001)]

dp[0] = 1
dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    dp[i] = dp[i-2] * 2 + dp[i-1]

print(dp[n] % 10007)

'''
점화식

1개 남았을때: 1
2개 남았을때: 3

4: 11
5: 21

'''