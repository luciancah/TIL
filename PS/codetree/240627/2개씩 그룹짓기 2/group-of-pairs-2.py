n = int(input())
arr = list(map(int, input().split()))
arr.sort()

arr1 = arr[:n]
arr2 = arr[n:]

max_diff = 999999999

# print(arr1,arr2)

for i in range(n):
    diff = abs(arr1[i] - arr2[i])
    max_diff = min(max_diff, diff)

print(max_diff)