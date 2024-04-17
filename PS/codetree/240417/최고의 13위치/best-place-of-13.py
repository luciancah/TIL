n = int(input())
arr = []
count = 0

for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n - 2):
        s = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        if s > count:
            count = s

print(count)