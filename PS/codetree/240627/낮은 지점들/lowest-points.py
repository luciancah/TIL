from collections import defaultdict

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dots = defaultdict(int)
for i in range(n):
    d = arr[i]
    if dots[d[0]]:
        if dots[d[0]] > d[1]:
            dots[d[0]] = d[1]
    else:
        dots[d[0]] = d[1]

print(sum(list(dots.values())))