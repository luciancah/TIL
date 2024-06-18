import sys

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

def init():
    dp[0][n-1] = grid[0][n-1]

    for i in range(n-2, -1, -1):
        # 일자로 내리기
        dp[0][i] = dp[0][i+1] + grid[0][i]
    for i in range(1, n):
        # 왼쪽으로
        dp[i][n-1] = dp[i-1][n-1] + grid[i][n-1]


init()

for i in range(1, n):
    for j in range(n-2, -1, -1):
        dp[i][j] = min(dp[i][j+1], dp[i-1][j]) + grid[i][j]

print(dp[n-1][0])