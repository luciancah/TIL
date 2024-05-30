n, m, t = list(map(int, input().split()))

dys, dxs = [-1, 1, 0, 0], [0, 0, -1, 1]
move_dirs = {'U': 0, 'D': 1, 'L': 2, 'R': 3}

def change_dir(curr_dir):
    direction_map = {
        'R': 'L',
        'L': 'R',
        'U': 'D',
        'D': 'U'
    }
    return direction_map[curr_dir]

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

grid = [[[] for _ in range(n)] for _ in range(n)]
balls = []

for i in range(m):
    r, c, d, w = list(map(str, input().split()))
    balls.append([i+1, int(r)-1, int(c)-1, d, int(w)])

for b in balls:
    grid[b[1]][b[2]].append(b[0])

def move_ball(curr_ball, r, c):
    d = curr_ball[3]
    ny, nx = r + dys[move_dirs[d]], c + dxs[move_dirs[d]]

    if in_range(ny, nx):
        return ny, nx
    else:
        curr_ball[3] = change_dir(d)
        return r, c

# for i in range(n):
#     print(*grid[i])
# print()

for _ in range(t):
    new_grid = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                for k in grid[i][j]:
                    ny, nx = move_ball(balls[k - 1], i, j)
                    new_grid[ny][nx].append(k)

    for i in range(n):
        for j in range(n):
            if len(new_grid[i][j]) > 1:
                # 방향: 번호 큰거
                # 웨이트: 구슬의 합
                new_grid[i][j].sort(key=lambda x: (-balls[x-1][0])) # -balls[x-1][4],
                sum_weight = 0
                for k in range(len(new_grid[i][j])):
                    sum_weight += balls[new_grid[i][j][k]-1][4]
                new_grid[i][j] = new_grid[i][j][:1]
                balls[new_grid[i][j][0]-1][4] = sum_weight

    grid = new_grid

# for i in range(n):
#     print(*grid[i])
# print()

# count = sum(len(grid[i][j]) for i in range(n) for j in range(n))
new_balls = []

for i in range(n):
    for j in range(n):
        if len(grid[i][j]) != 0:
            new_balls.append(*grid[i][j])

new_balls.sort(key=lambda x: -balls[x-1][4])

print(len(new_balls), balls[new_balls[0]-1][4])

# print(count)