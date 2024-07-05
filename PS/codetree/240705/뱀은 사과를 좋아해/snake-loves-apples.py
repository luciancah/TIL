n, m, k = map(int, input().split())
mat = []
for _ in range(n):
    mat.append([0 for _ in range(n)])
for _ in range(m):
    y, x = map(int, input().split())
    mat[y-1][x-1] = 1

time = 0
snake = [[0, 0]]
d = None
dxs, dys = [0, 0, 1, -1], [-1, 1, 0, 0] # U D R L
x, y = 0, 0

def turn(direction):
    if direction == 'U':
        d = 0
    elif direction == 'D':
        d = 1
    elif direction == 'R':
        d = 2
    elif direction == 'L':
        d = 3
    return d

def check_exit(row, col):
    if [row, col] in snake:
        print(time)
        exit()
    snake.append([row, col])

def check_apple(row, col):
    if row < 0 or row > n - 1 or col < 0 or col > n - 1:
        print(time)
        exit()
    if mat[row][col] == 1:
        mat[row][col] = 0
    else:
        snake.pop(0)

for _ in range(k):
    direction, offset = input().split()
    offset = int(offset)
    d = turn(direction)
    for _ in range(offset):
        time += 1
        nx, ny = x + dxs[d], y + dys[d]
        check_apple(ny, nx)
        check_exit(ny, nx)
        x, y = nx, ny
print(time)