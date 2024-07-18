n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

set1 = set(arr1)

for i in range(m):
    print(1 if arr2[i] in set1 else 0)