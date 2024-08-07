from sortedcontainers import SortedSet

n, m = map(int, input().split())
s = SortedSet([x for x in range(1, m+1)])
balls = list(map(int, input().split()))

for b in balls:
    s.remove(b)
    print(s[-1])