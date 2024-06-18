import sys

int_min = -sys.maxsize

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*n  for _ in range(n)]

def init():
    dp[0][0] = grid[0][0]

    for i in range(1, n):
        # 일자로 내리기
        dp[i][0] = dp[i-1][0] + grid[i][0]

    for i in range(1, n):
        # 대각선으로 내리기
        # dp[i][i] = dp[i-1][i-1] + a[i][i]
        dp[0][i] = dp[0][i-1] + grid[0][i]


init()
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]

# for i in range(n):
#     print(*dp[i])

ans = int_min
for j in range(n):
    ans = max(ans, dp[n-1][j])

print(ans)