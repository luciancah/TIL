from sortedcontainers import SortedSet
import sys

s = SortedSet([0])
n = int(input())
arr = list(map(int, input().split()))
ans = sys.maxsize

for e in arr:
    # print(s, e, s.bisect_right(e))
    right = s.bisect_right(e)

    if right == len(s):
        ans = min(ans, abs(s[right-1]-e))
    else:
        ans = min(ans, abs(s[right-1]-e), abs(s[right]-e))
    print(ans)
    s.add(e)