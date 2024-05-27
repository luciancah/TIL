import sys

n, m, r, c = list(map(int, input().split()))
moves = list(map(str, input().split()))
grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 나 / 좌우상하
curr_dice = [1, 4, 3, 5, 2]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

dys, dxs = [0, 0, -1, 1], [-1, 1, 0, 0]
direc = {'L': 0, 'R': 1, 'U': 2, 'D': 3}

def rotate_dice(curr_dice, direction):
    new_dice = [0] * 5
    if direction == 'L' or direction == 'R':
        new_dice[3] = curr_dice[3]
        new_dice[4] = curr_dice[4]
        if direction == 'R':
            new_dice[0] = curr_dice[1]
            new_dice[2] = curr_dice[0]
            new_dice[1] = 7 - curr_dice[0]
        elif direction == 'L':
            new_dice[0] = curr_dice[2]
            new_dice[1] = curr_dice[0]
            new_dice[2] = 7 - curr_dice[0]
    if direction == 'U' or direction == 'D':
        new_dice[1] = curr_dice[1]
        new_dice[2] = curr_dice[2]
        if direction == 'U':
            new_dice[0] = curr_dice[4]
            new_dice[3] = curr_dice[0]
            new_dice[4] = 7 - curr_dice[0]
        elif direction == 'D':
            new_dice[0] = curr_dice[3]
            new_dice[4] = curr_dice[0]
            new_dice[3] = 7 - curr_dice[0]
    # print(curr_dice, new_dice, direction)
    return new_dice


y, x = r-1, c-1

grid[y][x] = 7 - curr_dice[0]

for m in moves:
    # print(m, curr_dice)
    ny, nx = y + dys[direc[m]], x + dxs[direc[m]]
    # print(m, y, x, ny, nx)
    if not in_range(ny, nx):
        # print(ny, nx)
        ny, nx = y - dys[direc[m]], x - dxs[direc[m]]
        continue

    curr_dice = rotate_dice(curr_dice, m)
    grid[ny][nx] = 7 - curr_dice[0]
    y, x = ny, nx

    # for i in range(4):
    #     print(*grid[i])
    # print()

# print(grid)

ans = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] != 0:
            ans += grid[i][j]

print(ans)