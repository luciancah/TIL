n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

'''
dp[i][j] = i개 동전 사용해서 j라는 금액 만드는 경우의 수 <- 멤초
dp[i] = i 금액 만드는 경우의 수
'''

dp = [0 for _ in range(k+1)]

dp[0] = 1
for c in coins:
  for i in range(c, k+1):
    dp[i] = dp[i] + dp[i-c]

print(dp[k])