# 가능한 가짓수 구하는 문제 -> 2차원으로 해야댐
# dp[i][j] -> i번 숫자까지 고려했을 때 j가 나오는 서로 다른 가짓수
# 가짓수 : i번 숫자 뺀경우 / 더한경우

import sys

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

int_min = -sys.maxsize


dp = [[0 for _ in range(41)] for _ in range(n+1)]

# for i in range(n+1):
#     for j in range(41):
#         dp[i][j] = 0

dp[0][20] = 1
m += 20

for i in range(1, n+1):
    for j in range(0, 41):
        if j + arr[i] <= 40:
            dp[i][j] += dp[i-1][j + arr[i]]
        
        if j - arr[i] >= 0:
            dp[i][j] += dp[i-1][j - arr[i]]

print(dp[n][m])