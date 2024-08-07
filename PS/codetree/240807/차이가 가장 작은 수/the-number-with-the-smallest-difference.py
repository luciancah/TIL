import sys
from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = SortedSet([int(input()) for _ in range(n)])

ans = sys.maxsize
# print(arr)

for e in arr:
    min_idx = arr.bisect_left(e+m)
    if min_idx != len(arr):
        ans = min(ans, arr[min_idx] - e)
    
    max_idx = arr.bisect_right(e-m)-1
    if max_idx >= 0:
        ans = min(ans, e-arr[max_idx])


print(ans if ans != sys.maxsize else -1)