from collections import Counter

t = int(input())

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

for i in range(t):
    n, m = list(map(int, input().split()))
    balls = []
    grid = [['0'] * n for _ in range(n)]

    for i in range(m):
        y, x, dirr = list(map(str, input().split()))
        y, x = int(y) - 1, int(x) - 1
        grid[y][x] = dirr

    for _ in range(n*2):
        new_grid = [['0'] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if len(grid[i][j]) == 1 and grid[i][j] != '0':
                    ny, nx = i + dys[move_dirs[grid[i][j]]], j + dxs[move_dirs[grid[i][j]]]

                    if in_range(ny, nx):
                        if new_grid[ny][nx] == '0':
                            new_grid[ny][nx] = grid[i][j]
                        else:
                            new_grid[ny][nx] += grid[i][j]
                    else:
                        if new_grid[i][j] == '0':
                            new_grid[i][j] = change_dir(grid[i][j])
                        else:
                            new_grid[i][j] += change_dir(grid[i][j])

        for i in range(n):
            for j in range(n):
                if len(grid[i][j]) > 1:
                    grid[i][j] = '0'

        grid = new_grid

    count = 0
    for i in range(n):
        for j in range(n):
            if len(grid[i][j]) == 1 and grid[i][j] != '0':
                count += 1

    print(count)