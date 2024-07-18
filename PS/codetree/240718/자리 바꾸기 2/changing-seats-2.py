n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

seats = [[x] for x in range(n+1)]

for _ in range(3):
    for a in arr:
        x = seats[a[0]][-1]
        y = seats[a[1]][-1]
        
        seats[a[0]].append(y)
        seats[a[1]].append(x)

seats2 = [set(x) for x in seats]
counts = [0 for _ in range(n+1)]

for se in seats2:
    for s in se:
        counts[s] += 1

for c in counts[1:]:
    print(c)