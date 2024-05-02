n, m = map(int, input().split())
ans_mat = [[0 for col in range(m)] for row in range(n)]
x, y = 0, 0
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
mapper = {
    0 : 'R',
    1 : 'D',
    2 : 'L',
    3 : 'U'
}
d = 0
for i in range(n * m):
    ans_mat[y][x] = i + 1
    # print(x, y, d)
    # print(ans_mat[y])
    nx, ny = x + dxs[d], y + dys[d]
    # print(nx, ny)
    # print('--------------------')
    if nx >= 0 and nx <= m - 1 and ny >= 0 and ny <= n - 1:
        if ans_mat[ny][nx] != 0:
            d += 1
            d %= 4
            x, y = x + dxs[d], y + dys[d]
        else:
            x, y = nx, ny
    else:
        d += 1
        d %= 4
        x, y = x + dxs[d], y + dys[d]
for c in ans_mat:
    print(*c)