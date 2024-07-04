from collections import defaultdict
from bisect import bisect_left,bisect_right

t = int(input())
n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))


def lower_bound(arr, target):
  index = len(arr)
  left, right = 0, len(arr) -1

  while left <= right:
    mid = (left + right) // 2
    if arr[mid] >= target:
      index = min(index, mid)
      right = mid - 1
    else:
      left = mid + 1
  
  return index

def upper_bound(arr, target):
  index = len(arr)
  left, right = 0, len(arr) - 1

  while left <= right:
    mid = (left + right) // 2
    if arr[mid] > target:
      index = min(index, mid)
      right = mid - 1
    else:
      left = mid + 1
  
  return index



pa = []
pb = []

for i in range(n):
  s = 0
  for j in range(i, n):
    s += arr1[j]
    pa.append(s)


for i in range(m):
  s = 0
  for j in range(i, m):
    s += arr2[j]
    pb.append(s)

pb.sort()
ans = 0

for i in range(len(pa)):
  res = t - pa[i]
  ans += bisect_right(pb, res) - bisect_left(pb, res)

print(ans)