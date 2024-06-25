import sys

n = int(input())
arr = list(map(int, input().split()))
sum_arr = sum(arr)

if sum_arr % 2 == 1:
    print('No')
    sys.exit()

dp = [0 for _ in range(sum_arr + 1)]
dp[0] = 1

for j in range(n):
    for i in range(sum_arr, -1, -1):
        if i - arr[j] < 0:
            continue
        if not dp[i-arr[j]]:
            continue
        dp[i] = 1

ans = 'Yes' if dp[sum_arr // 2] else 'No'
 
# print(dp)
print(ans)