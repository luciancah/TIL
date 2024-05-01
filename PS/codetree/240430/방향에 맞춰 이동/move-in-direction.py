n = int(input())
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
x, y = 0, 0
for i in range(n):
    direction, offset = input().split(' ')
    offset = int(offset)
    if direction == 'N':
        direction = 3
    elif direction == 'W':
        direction = 2
    elif direction == 'S':
        direction = 1
    else:
        direction = 0
    x += dx[direction] * offset
    y += dy[direction] * offset
print(x, y)