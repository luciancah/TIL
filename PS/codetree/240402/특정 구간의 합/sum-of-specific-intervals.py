n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr2 = []

for i in range(m):
    arr2.append(list(map(int, input().split())))


prefixSum = [0] * (len(arr) + 1)
for i in range(1, len(arr) + 1):
    prefixSum[i] = arr[i-1] + prefixSum[i-1]

for i in range(m):
    print(prefixSum[arr2[i][1]] - prefixSum[arr2[i][0]-1])