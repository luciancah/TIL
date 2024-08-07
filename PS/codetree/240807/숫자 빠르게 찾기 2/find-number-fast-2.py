from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = list(map(int, input().split()))
s = SortedSet(arr)

for _ in range(m):
    elem = int(input())

    if s.bisect_left(elem) != len(s):
        print(s[s.bisect_left(elem)])
    else:
        print(-1)