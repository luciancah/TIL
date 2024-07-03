'''
-  dp[i][j][k] -> i번 애 까지 보고 j명 축구 k명 야구에 넣었을 때 두 팀 능력치의 합
j + k < i
'''

n = int(input())
arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: (x[0], x[1]))

dp = [[[0 for _ in range(10)] for _ in range(12)] for _ in range(n+1)]
dp[0][0][0] = 0
for i in range(1, n+1):
    for j in range(min(i+1, 12)):
        for k in range(min(i+1, 10)):
            dp[i][j][k] = dp[i-1][j][k]
            if j > 0:
                dp[i][j][k] = max(dp[i-1][j-1][k] + arr[i][0], dp[i][j][k])
            if k > 0:
                dp[i][j][k] = max(dp[i-1][j][k-1] + arr[i][1], dp[i][j][k])
            # if i > k or i > j:
            #     dp[i][j][k] = max(dp[i-1][j-1][k] + arr[i][0], dp[i-1][j][k-1] + arr[i][1], dp[i][j][k])
            # if i > j:
            #     dp[i][j][k] = max(dp[i-1][j-1][k] + arr[i][0], dp[i][j][k])

# for i in range(n):
#     print(*dp[i])
# print()
# print(dp)
print(dp[n][11][9])
# print()
# print(dp[21])