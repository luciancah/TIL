import sys

n, m = map(int, input().split())
dp = [0] * (m+1)
coin = [0] + list(map(int, input().split()))

def init():
    for i in range(m+1):
        dp[i] = sys.maxsize
    dp[0] = 0

init()

for i in range(1, m+1):
    for j in range(1, n+1):
        if i >= coin[j]:
            if dp[i-coin[j]] == sys.maxsize:
                continue
            dp[i] = min(dp[i], dp[i-coin[j]] + 1)

ans = dp[m]

if ans == sys.maxsize:
    ans = -1

print(ans)