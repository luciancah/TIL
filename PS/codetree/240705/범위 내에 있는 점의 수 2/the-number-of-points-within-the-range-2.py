from collections import defaultdict

n, q = map(int, input().split())
arr = list(map(int, input().split()))
lines = [list(map(int, input().split())) for _ in range(q)]

dots = defaultdict(bool)
for a in arr:
    dots[a] = True

narr = [1 if dots[i] else 0 for i in range(1000005)]
ps = [0 for _ in range(1000005)]

for i in range(1, 1000001):
    ps[i] = ps[i-1] + narr[i]

# print(narr)
# print(ps)

for l in lines:
    res = ps[l[1]] - ps[l[0]] + 1 if narr[l[0]] == 1 else ps[l[1]] - ps[l[0]]
    print(res if res >= 0 else 0)