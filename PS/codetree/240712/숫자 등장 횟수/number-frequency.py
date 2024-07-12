from collections import defaultdict

n, m = map(int, input().split())
arr = list(map(int, input().split()))
inputs = list(map(int, input().split()))

d = defaultdict(int)

for a in arr:
    d[a] += 1

print(' '.join(map(str, [d[i] for i in inputs])))