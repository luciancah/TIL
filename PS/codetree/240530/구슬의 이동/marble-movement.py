n, m, t, z = list(map(int, input().split()))

# 상하좌우
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

grid = [[[]] * n for _ in range(n)]
balls = []

for i in range(m):
    r, c, d, v = list(map(str, input().split()))
    balls.append([i+1, int(r)-1, int(c)-1, d, int(v)])

for b in balls:
    grid[b[1]][b[2]] = [b[0]]

def move_ball(curr_ball, r, c):
    d, v = curr_ball[3], curr_ball[4]

    if d == 'R':
        share = (c + v) // (n - 1)
        remainder = (c + v) % (n - 1)
        if share % 2 == 0:
            d = 'R'
            c = remainder
        else:
            d = 'L'
            # balls[grid[r][c][0]-1][3] = 'L'
            curr_ball[3] = 'L'
            c = n-1-remainder
    
    elif d == 'L':
        share = (n - 1 - c + v) // (n - 1)
        remainder = (n - 1 - c + v) % (n - 1)
        if share % 2 == 0:
            d = 'L'
            c = n - 1 - remainder
        else:
            d = 'R'
            # balls[grid[r][c][0]-1][3] = 'R'
            curr_ball[3] = 'R'
            c = remainder

    elif d == 'U':
        share = (n - 1 - r + v) // (n - 1)
        remainder = (n - 1 - r + v) % (n - 1)
        if share % 2 == 0:
            d = 'U'
            r = n-1-remainder
        else:
            d = 'D'
            # balls[grid[r][c][0]-1][3] = 'D'
            curr_ball[3] = 'D'
            r = remainder

    elif d == 'D':
        share = (r + v) // (n - 1)
        remainder = (r + v) % (n - 1)

        if share % 2 == 0:
            d = 'D'
            r = remainder
        else:
            d = 'U'
            # balls[grid[r][c][0]-1][3] = 'U'
            curr_ball[3] = 'U'
            r = n - 1 - remainder
    return (r, c)

for _ in range(t):
    new_grid = [[[]] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if len(grid[i][j]) != 0:
                for k in range(len(grid[i][j])):
                    ny, nx = move_ball(balls[grid[i][j][k]-1], i, j)
                    new_grid[ny][nx] = new_grid[ny][nx] + [grid[i][j][k]]

    for i in range(n):
        for j in range(n):
            if len(new_grid[i][j]) > z:
                new_grid[i][j].sort(key=lambda x: (-balls[x-1][4], -balls[x-1][0]))
                new_grid[i][j] = new_grid[i][j][0:z]


    grid = new_grid

count = 0
for i in range(n):
    for j in range(n):
        if len(grid[i][j]) != 0:
            count += len(grid[i][j])

print(count)