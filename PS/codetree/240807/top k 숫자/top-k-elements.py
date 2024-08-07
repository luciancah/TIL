from sortedcontainers import SortedSet

n, k = map(int, input().split())
arr = list(map(int, input().split()))

s = SortedSet(arr)
s = list(s)
s.reverse()
print(' '.join(list(map(str, s[:k]))))