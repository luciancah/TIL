n, m, t = list(map(int, input().split()))
grid = []
balls_grid = [[0] * n for _ in range(n)]

for _ in range(n):
    grid.append(list(map(int, input().split())))

balls = []

for i in range(m):
    balls.append(list(map(int, input().split())))
    balls_grid[balls[i][0]-1][balls[i][1]-1] = 1

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

dys, dxs = [-1, 1, 0, 0], [0, 0, -1, 1]

def check_near(y, x):
    max_near = [0, y, x]
    for i in range(4):
        ny, nx = y + dys[i], x + dxs[i]
        if not in_range(ny, nx):
            continue
        temp = max_near[0]
        max_near[0] = max(grid[ny][nx], max_near[0])

        if max_near[0] != temp:
            max_near[1], max_near[2] = ny, nx

    return max_near[1], max_near[2]

def find_duplicate(arr):
    duplicates = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                duplicates.append(arr[i])

    return duplicates

for _ in range(t):
    new_grid = [[0] * n for _ in range(n)]
    new_balls = []
    for i in range(n):
        for j in range(n):
            if balls_grid[i][j] == 1:
                ny, nx = check_near(i, j)
                new_balls.append([ny, nx])
                new_grid[ny][nx] = 1

    dups = find_duplicate(new_balls)
    for d in dups:
        new_grid[d[0]][d[1]] = 0
    balls_grid = new_grid

count = 0
for i in range(n):
    for j in range(n):
        if balls_grid[i][j] != 0:
            count += 1

print(count)