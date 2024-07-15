from collections import defaultdict

n = int(input())
arr = [list(input()) for _ in range(n)]

d = defaultdict(int)

for i in range(n):
    arr[i].sort()
    d[''.join(map(str,arr[i]))] += 1

d2 = list(sorted(d.items(), key=lambda x: -x[1]))
print(d2[0][1])