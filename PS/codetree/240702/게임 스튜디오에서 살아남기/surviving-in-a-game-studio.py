n = int(input())
mod = 10**9 + 7

# dp[i][j][k] => i일차 j개 T일때 k개 연속 B일때 안짤린 가짓수
# dp = [[0] * 2 for _ in range(n+1)]
dp = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(1005)]

dp[0][1][0] = 1
dp[0][0][1] = 1
dp[0][0][0] = 1

for i in range(n):
    for j in range(3):
        for k in range(3):
            # T 일때
            dp[i+1][j+1][0] = (dp[i+1][j+1][0] + dp[i][j][k]) % mod
            # G 일때
            dp[i+1][j][0] = (dp[i+1][j][0] + dp[i][j][k]) % mod
            if k < 2:
                dp[i+1][j][k+1] = (dp[i+1][j][k+1] + dp[i][j][k]) % mod

# print(dp[n-1])
ans = 0
for j in range(3):
    for k in range(3):
        ans = (ans + dp[n-1][j][k]) % mod

print(ans)