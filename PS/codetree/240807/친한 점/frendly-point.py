from sortedcontainers import SortedSet

n, m = map(int, input().split())
dots = [tuple(map(int, input().split())) for _ in range(n)]
oprs = [tuple(map(int, input().split())) for _ in range(m)]

dots = SortedSet(dots)
for e in oprs:
    if dots.bisect_left(e) < len(dots):
        print(" ".join(map(str, dots[dots.bisect_left(e)])))
    else:
        print("-1 -1")