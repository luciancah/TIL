from collections import defaultdict

n, m = map(int, input().split())
arr = [input() for _ in range(n)]
inputs = [input() for _ in range(m)]

d = defaultdict(int)
d2 = defaultdict(int)

for i, e in enumerate(arr):
    d[i+1] = e

for i, e in enumerate(arr):
    d2[e] = i+1

for i in inputs:
    if i.isnumeric():
        print(d[int(i)])
    else:
        print(d2[i])