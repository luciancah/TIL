from collections import defaultdict

n, k, b = map(int, input().split())
subs = defaultdict(int)
for _ in range(b):
    subs[int(input())] = 1

arr = [1 if not subs[i] else 0 for i in range(1, n+1)]
ps = [0 for _ in range(n+1)]

for i in range(1, n+1):
    ps[i] = ps[i-1] + arr[i-1]

ans = 0

for i in range(1, n-k+1):
    ans = max(ps[i+k] - ps[i], ans)

print(k - ans)