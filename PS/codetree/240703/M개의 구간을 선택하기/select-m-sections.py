import sys

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# dp[i][j][k] => i번 숫자까지 보고, j개 구간 지금까지 선택했는데, 마지막으로 선택한 위치가 k일때 최대의 합
# 말고 -> i번 위치가 마지막 구간에 포함 / 미포함
dp = [[[-sys.maxsize for _ in range(2)] for _ in range(m + 1)] for _ in range(n + 1)]
# dp[0][0][0] = 0
for i in range(n+1):
    dp[i][0][0] = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j][1] = max(dp[i-1][j-1][0] + arr[i], dp[i-1][j][1] + arr[i])

        dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1])


print(max(dp[n][m]))