n, r, c = map(int, input().split())
m = []
for _ in range(n):
    m.append([int(x) for x in input().split()])
x = c -1
y = r - 1
dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0] #상하좌우
ret = []
ret.append(m[y][x])
while True:
    prev_x, prev_y = x, y
    for i in range(4):
        nx, ny = x + dxs[i], y + dys[i]
        if nx > n - 1 or ny > n -1 or nx < 0 or ny < 0:
            continue
        # print(m[ny][nx], m[y][x])
        if m[ny][nx] > m[y][x]:
            x, y = nx, ny
            break
    if prev_x == x and prev_y == y:
        print(*ret)
        exit()
    else:
        ret.append(m[y][x])