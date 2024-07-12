from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))

d = defaultdict(int)

ans = 0
for e in arr:
    diff = k - e

    if diff in d:
        ans += d[diff]
    
    if e in d:
        d[e] += 1
    else:
        d[e] = 1

print(ans)