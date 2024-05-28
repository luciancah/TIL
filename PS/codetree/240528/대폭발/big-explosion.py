from copy import deepcopy
from math import pow

n, m, r, c = list(map(int, input().split()))
grid = [[0] * n for _ in range(n)]

dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

def update_grid(grid, t):
    new_grid = deepcopy(grid)

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                for k in range(4):
                    ny, nx = i + dys[k]*int(pow(2, t-1)), j + dxs[k]*int(pow(2, t-1))
                    if in_range(ny, nx):
                        # print(i, j, ny, nx, t, k)
                        new_grid[ny][nx] = 1

    # for i in range(n):
    #     print(*new_grid[i])
    # print()
    return new_grid

y, x = r-1, c-1
grid[y][x] = 1

for t in range(m+1):
    # print('t', t)
    grid = update_grid(grid, t)


count = 0

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            count += 1

print(count)