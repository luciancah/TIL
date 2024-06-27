n, m = map(int, input().split())
a_arr = [list(map(int, input().split())) for _ in range(n)]
b_arr = [list(map(int, input().split())) for _ in range(m)]

total_time = 0
for i in range(n):
    total_time += a_arr[i][1]

grid = [[-1] * (total_time) for _ in range(2)]

cur = -1
dist = 0
for i in range(n):
    for j in range(a_arr[i][1]):
        cur += 1
        dist += a_arr[i][0]
        # print(cur, dist)
        grid[0][cur] = dist

cur = -1
dist = 0
for i in range(m):
    for j in range(b_arr[i][1]):
        cur += 1
        dist += b_arr[i][0]
        # print(cur, dist)
        grid[1][cur] = dist

ans = 9
count = 0

# print(grid)

for a, b in zip(grid[0], grid[1]):
    if a == b:
        new_ans = 0
    if a > b:
        new_ans = 1
    if a < b:
        new_ans = -1
    # print(a, b, ans, new_ans)
    if new_ans != ans:
        # print('changed', a, b)
        ans = new_ans
        count += 1

print(count)