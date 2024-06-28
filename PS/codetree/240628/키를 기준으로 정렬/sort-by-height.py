n = int(input())
arr = [list(map(str, input().split())) for _ in range(n)]

arr.sort(key=lambda x: x[1])
for i in range(n):
    print(' '.join(arr[i]))