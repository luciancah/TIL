n = int(input())
grid = [
    [0] * (n+1) for _ in range(n+1)
]

for i in range(n):
    arr = (list(map(int, input().split())))
    for j in range(n):
        grid[i+1][j+1] = arr[j]

sq = list(map(int, input().split()))

sq_cor = [[sq[0], sq[1]], [sq[0] - sq[2], sq[1] + sq[2]], [sq[0] - sq[2] - sq[3], sq[1] + sq[2]- sq[3]], [sq[0] - sq[2] - sq[3] + sq[4], sq[1] + sq[2]- sq[3] - sq[4]]]

def rotate_ccw(c0x, c0y, c1x, c1y, c2x, c2y, c3x, c3y):
    temp = grid[c0x][c0y]

    count = 0
    for ul in range(c0x, c3x, -1):
        # 4, 2 -> 3, 1
        grid[ul][c0y-count] = grid[ul-1][c0y-count-1]
        count += 1

    count = 0
    for ur in range(c3x, c2x, -1):
        # 3, 1 -> 1, 3
        grid[ur][c3y+count] = grid[ur-1][c3y+count+1]
        count += 1

    count = 0
    for dr in range(c2x, c1x):
        # 1, 3 -> 2, 4
        grid[dr][c2y+count] = grid[dr+1][c2y+count+1]
        count += 1

    count = 0
    for dl in range(c1x, c0x):
        # 2, 4 -> 4, 2
        grid[dl][c1y-count] = grid[dl+1][c1y-count-1]
        count += 1

    grid[c0x-1][c0y+1] = temp

def rotate_cw(c0x, c0y, c1x, c1y, c2x, c2y, c3x, c3y):
    temp = grid[c0x][c0y]

    count = 0
    for dl in range(c0x, c1x, -1):
        # 4, 2 -> 2, 4
        grid[dl][c0y+count] = grid[dl-1][c0y+count+1]
        count += 1

    count = 0
    for dr in range(c1x, c2x, -1):
        # 2, 4 -> 1, 3
        grid[dr][c1y-count] = grid[dr-1][c1y-count-1]
        count += 1

    count = 0
    for ur in range(c2x, c3x):
        # 1, 3 -> 3, 1
        grid[ur][c2y-count] = grid[ur+1][c2y-count-1]
        count += 1

    count = 0
    for ul in range(c3x, c0x):
        # 3, 1 -> 4, 2
        grid[ul][c3y+count] = grid[ul+1][c3y+count+1]
        count += 1

    grid[c0x-1][c0y-1] = temp


if sq[-1] == 0:
    rotate_ccw(sq_cor[0][0], sq_cor[0][1], sq_cor[1][0], sq_cor[1][1], sq_cor[2][0], sq_cor[2][1], sq_cor[3][0], sq_cor[3][1])
else:
    rotate_cw(sq_cor[0][0], sq_cor[0][1], sq_cor[1][0], sq_cor[1][1], sq_cor[2][0], sq_cor[2][1], sq_cor[3][0], sq_cor[3][1])


for i in range(1, n+1):
    print(*grid[i][1:])