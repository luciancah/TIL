import sys

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

prefix_sum = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + arr[i-1][j-1]

max_ans = -sys.maxsize
for i in range(n+1-k):
    for j in range(n+1-k):
        max_ans = max(max_ans, prefix_sum[i+k][j+k] + prefix_sum[i][j] - prefix_sum[i+k][j] - prefix_sum[i][j+k])

print(max_ans)