from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))

d = defaultdict(int)
for e in arr:
    d[e] += 1

d2 = list(d.items())
d2.sort(key=lambda x: (-x[1], -x[0]))

print(' '.join(map(str, [x[0] for x in d2[:k]])))