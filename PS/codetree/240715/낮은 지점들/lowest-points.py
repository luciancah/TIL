from collections import defaultdict

n = int(input())
dots = [list(map(int, input().split())) for _ in range(n)]

d = defaultdict(int)
for x, y in dots:
    d[x] = y if d[x] == 0 else min(d[x], y)

print(sum(list(d.values())))