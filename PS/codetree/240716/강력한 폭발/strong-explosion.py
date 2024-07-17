n = int(input())
mat = []
for _ in range(n):
    mat.append([int(x) for x in input().split()])
max_area = 0

COL = 0
CROSS = 1
X = 2

def boom(row, col, buf, bomb_type):
    buf[row][col] = 2
    if bomb_type == COL:
        for i in range(row - 2, row + 3):
            if i >= 0 and i <= n - 1 and buf[i][col] != 1: buf[i][col] = 2
    elif bomb_type == CROSS:
        if row > 0 and buf[row-1][col] != 1: buf[row - 1][col] = 2
        if row < n - 1 and buf[row+1][col] != 1: buf[row + 1][col] = 2
        if col > 0 and buf[row][col-1] != 1: buf[row][col - 1] = 2
        if col < n - 1 and buf[row][col+1] != 1: buf[row][col + 1] = 2
    else:
        if row > 0 and col > 0 and buf[row-1][col-1] != 1: buf[row - 1][col - 1] = 2
        if row > 0 and col < n - 1 and buf[row-1][col+1] != 1: buf[row - 1][col + 1] = 2
        if row < n - 1 and col > 0 and buf[row+1][col-1] != 1: buf[row + 1][col - 1] = 2
        if row < n - 1 and col < n - 1 and buf[row+1][col+1] != 1: buf[row + 1][col + 1] = 2

def check(row, col, buf):
    global max_area
    for row in range(n):
        for col in range(n):
            if buf[row][col] == 1:
                type_0 = [arr[:] for arr in buf]
                type_1 = [arr[:] for arr in buf]
                type_2 = [arr[:] for arr in buf]
                boom(row, col, type_0, COL)
                boom(row, col, type_1, CROSS)
                boom(row, col, type_2, X)
                check(row, col, type_0)
                check(row, col, type_1)
                check(row, col, type_2)
                return
    region_max = 0
    for i in range(n):
        for j in range(n):
            if buf[i][j] == 2: region_max += 1
    max_area = max(max_area, region_max)

check(0, 0, mat)
print(max_area)