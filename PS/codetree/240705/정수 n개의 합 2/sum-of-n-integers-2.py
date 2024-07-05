import sys

n, k = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [0 for _ in range(n+1)]

for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + arr[i]

max_ans = -sys.maxsize
for i in range(n-k):
    max_ans = max(prefix_sum[i+k] - prefix_sum[i], max_ans)

print(max_ans)