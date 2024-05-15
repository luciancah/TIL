n, m = list(map(int, input().split()))
arr = []
max_count = 0

for _ in range(n):
    arr.append(list(map(int, input().split())))

# 일자모양 탐색

# 가로 탐색
for i in range(n):
    for j in range(m-2):
        count_horizontal = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        max_count = max(max_count, count_horizontal)

# 세로 탐색
for i in range(n-2):
    for j in range(m):
        count_vertical = arr[i][j] + arr[i+1][j] + arr[i+2][j]
        max_count = max(max_count, count_vertical)

# ㄴ자모양 탐색
for i in range(n-1):
    for j in range(m-1):
        count1 = arr[i][j] + arr[i+1][j] + arr[i][j+1]
        count2 = arr[i][j] + arr[i+1][j] + arr[i+1][j+1]
        count3 = arr[i][j] + arr[i][j+1] + arr[i+1][j+1]
        count4 = arr[i+1][j] + arr[i][j+1] + arr[i+1][j+1]
        max_count = max(max_count, count1, count2, count3, count4)

print(max_count)