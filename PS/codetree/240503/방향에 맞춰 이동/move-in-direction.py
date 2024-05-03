n = int(input())
x, y = 0, 0

dx = [1, -1,  0, 0]
dy = [0,  0, -1, 1]

for _ in range(n):
    dir, dist = list(input().split())
    dist = int(dist)

    if dir == 'E':
        move_dir = 0
    elif dir == 'W':
        move_dir = 1
    elif dir == 'S':
        move_dir = 2
    else:
        move_dir = 3

    x += dx[move_dir] * dist
    y += dy[move_dir] * dist

print(x, y)