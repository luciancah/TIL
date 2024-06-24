n, m = map(int, input().split())
nums = list(map(int, input().split()))
dp = [10001 for _ in range(m+1)]
dp[0] = 0

for i in range(n):
    for j in range(m, -1, -1):
        if j >= nums[i]:
            dp[j] = min(dp[j], dp[j-nums[i]] + 1)

if dp[-1] == 10001:
    print('No')
else:
    print('Yes')