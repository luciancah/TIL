import sys

DIR_NUM = 4

n = int(input())
curr_x, curr_y = tuple(map(int, input().split()))
a = [
    [0 for _ in range(n + 1)]
    for _ in range(n + 1)
]

visited = [
    [
        [False for _ in range(DIR_NUM)]
        for _ in range(n + 1)
    ]
    for _ in range(n + 1)
]
elapsed_time = 0

curr_dir = 0

def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n

def wall_exist(x, y):
    return in_range(x, y) and a[x][y] == '#'

def simulate():
    global curr_x, curr_y, curr_dir, elapsed_time

    if visited[curr_x][curr_y][curr_dir]:
        print(-1)
        sys.exit(0)
    
    visited[curr_x][curr_y][curr_dir] = True
    
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    
    next_x, next_y = curr_x + dxs[curr_dir], curr_y + dys[curr_dir]
    
    if wall_exist(next_x, next_y):
        curr_dir = (curr_dir - 1 + 4) % 4
    
    elif not in_range(next_x, next_y):
        curr_x, curr_y = next_x, next_y
        elapsed_time += 1

    else:
        rx = next_x + dxs[(curr_dir + 1) % 4]
        ry = next_y + dys[(curr_dir + 1) % 4]
    
        if wall_exist(rx, ry):
            curr_x, curr_y = next_x, next_y
            elapsed_time += 1
        
        else:
            curr_x, curr_y = rx, ry
            curr_dir = (curr_dir + 1) % 4
            elapsed_time += 2


for i in range(1, n + 1):
    given_row = input()
    for j, elem in enumerate(given_row, start = 1):
        a[i][j] = elem

while in_range(curr_x, curr_y):
    simulate()

print(elapsed_time)