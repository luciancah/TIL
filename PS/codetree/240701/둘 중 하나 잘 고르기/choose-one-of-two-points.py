n = int(input())
arr =[[0,0]] +  [list(map(int, input().split())) for _ in range(n*2)]

# dp[i][j] = 빨간색 i번까지 봤을 때 빨간색 j개 뽑았을때 최대의 합, 답: dp[2n][n]

dp = [[-1] * (2*n+1) for _ in range(2*n+1)]
dp[0][0] = 0

# for i in range(1, 2*n+1):
#     dp[i][0] = dp[i-1][0] + arr[i][0]
#     dp[0][i] = dp[0][i-1] + arr[i][1]

for i in range(1, 2*n+1):
    for j in range(i+1):
        # # i번 빨간색 뽑고 j 안뽑는 경우
        if j > 0:
            dp[i][j] = max(dp[i-1][j-1] + arr[i][0], dp[i][j])
        if i -j > 0:
            dp[i][j] = max(dp[i-1][j] + arr[i][1], dp[i][j])

print(dp[2*n][n])