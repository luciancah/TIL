from collections import deque

n, m, k = list(map(int, input().split()))
apples = []
grid = [[0] * n for _ in range(n)]
for _ in range(m):
    apples.append(list(map(int, input().split())))
moves = []
for _ in range(k):
    moves.append(list(map(str, input().split())))

for m in moves:
    m[1] = int(m[1])


dys, dxs = [-1, 1, 0, 0], [0, 0, 1, -1]
move_dirs = {'U': 0, 'D': 1, 'R': 2, 'L': 3}

snakes = [[0, 0]]
snakesq = deque(snakes)

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

def in_snake(y, x):
    if [y, x] in snakesq:
        return True
    else:
        return False

def move_snake(flag, grid, count, m, y, x):
    dirr = move_dirs[m[0]] # R : 2

    for i in range(m[1]):
        ny, nx = y + dys[dirr], x + dxs[dirr]
        
        if not in_range(ny, nx):
            flag = False
            count += 1
            return (y, x, count, flag, grid)

        # 가는거
        if not(grid[ny][nx] == 1):
            snakesq.popleft() 
        else:
            grid[ny][nx] = 0

        if in_snake(ny, nx):
            flag = False
            count += 1
            return (y, x, count, flag, grid)

        snakesq.append([ny, nx])
        count += 1
        y, x = ny, nx
    return (y, x, count, flag, grid)



count = 0
y, x = 0, 0
flag = True

for a in apples:
    grid[a[0]-1][a[1]-1] = 1


for m in moves:
    if flag == False:
        break
    y, x, count, flag, grid = move_snake(flag, grid, count, m, y, x)

print(count)