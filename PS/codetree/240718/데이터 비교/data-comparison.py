n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

set1 = set(arr1)

res = []
for i in range(m):
    if arr2[i] in set1:
        res.append('1')
    else:
        res.append('0')

print(" ".join(res))