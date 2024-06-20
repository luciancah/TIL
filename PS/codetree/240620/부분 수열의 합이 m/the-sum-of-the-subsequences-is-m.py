MAX_ANS = 10001
n, m = map(int, input().split())
coin = list(map(int, input().split()))
dp = [MAX_ANS for _ in range(m + 1)]
dp[0] = 0

for i in range(n):
    for j in range(m, -1, -1):
        if j >= coin[i]:
            dp[j] = min(dp[j], dp[j - coin[i]] + 1)

min_cnt = dp[m]

if min_cnt == MAX_ANS:
    min_cnt = -1

print(min_cnt)