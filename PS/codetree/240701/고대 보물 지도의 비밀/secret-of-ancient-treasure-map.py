import sys
int_min = -sys.maxsize

n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# dp[i][j] = i위치에서 j개 음수가 있을 때 연속합 중 최댓값

dp = [[int_min] * (k+1) for i in range(n+1)]

dp[0][0] = 0
ans = int_min

for i in range(1, n+1):
    is_negative = 1 if arr[i] < 0 else 0
    for j in range(k+1):
        if is_negative:
            if j-1 >= 0:
                dp[i][j] = max(arr[i], dp[i-1][j-1] + arr[i])
        else: 
            dp[i][j] = max(arr[i], dp[i-1][j] + arr[i])
        ans = max(dp[i][j], ans)

# print(dp)
print(ans)