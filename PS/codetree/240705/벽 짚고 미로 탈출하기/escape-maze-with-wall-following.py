n = int(input())
y, x = map(int, input().split())
x -= 1
y -= 1
mat = []
for _ in range(n):
    buf = input()
    lst = []
    for c in buf:
        lst.append(c)
    mat.append(lst)

dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1] # E, N, W, S
time = 0
d = 0
bread_crumbs = []

def turn(is_clockwise, d):
    if is_clockwise == 1:
        d -= 1
        if d < 0:
            d = 4 + d
    else:
        d += 1
        if d > 3:
            d %= 4
    return d

while True:
    if [x, y, dxs[d], dys[d]] in bread_crumbs:
        # print([x, y, dxs[d], dys[d]])
        # for l in bread_crumbs:
        #     print(*l)
        print(-1)
        break
    bread_crumbs.append([x, y, dxs[d], dys[d]])
    nx, ny = x + dxs[d], y + dys[d]
    # print('curr', y, x, 'new', ny, nx, d)
    if ny >= n or nx >= n or ny < 0 or nx < 0:
        # print(ny, nx, y, x)
        time += 1
        print(time)
        break
    elif mat[ny][nx] == '#':
        d = turn(-1, d)
    elif mat[ny][nx] == '.':
        time += 1
        x, y = nx, ny
        r_x, r_y = x + dxs[turn(1, d)], y + dys[turn(1, d)]
        # print(y, x, r_y, r_x, dys[d], dxs[d], 'right')
        if mat[r_y][r_x] == '.':
            d = turn(1, d)
    else:
        print('IMPOSSIBLE')
        break