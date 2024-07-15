n, m, t = map(int, input().split())
mat = [[0 for _ in range(n)] for _ in range(n)]

def print_mat(mat):
    print('-------------------')
    for item in mat:
        print(*item)

dxs, dys = [0, 0, 1, -1], [-1, 1, 0, 0] # U D R L
U, D, R, L = 0, 1, 2, 3

remain = m
max_w = 0

for i in range(m):
    row, col, d, w = input().split()
    row, col, w = int(row) - 1, int(col) - 1, int(w)
    if w > max_w: max_w = w
    mat[row][col] = [d, w, i]

def move(d, row, col):
    if d == 'U': nd = U
    elif d == 'D': nd = D
    elif d == 'R' : nd = R
    else : nd = L
    ny, nx = row + dys[nd], col + dxs[nd]
    if ny < 0:
        ny = row
        d = 'D'
    elif ny > n - 1:
        ny = row
        d = 'U'
    elif nx < 0:
        nx = col
        d = 'R'
    elif nx > n - 1:
        nx = col
        d = 'L'
    return (ny, nx, d)

# print_mat(mat)
for _ in range(t):
    buf = [[0 for _ in range(n)] for _ in range(n)]
    for row in range(n):
        for col in range(n):
            if mat[row][col] != 0:
                d = mat[row][col][0]
                w = mat[row][col][1]
                idx = mat[row][col][2]
                ny, nx, d = move(d, row, col)
                # if ny != row or nx != col:
                if buf[ny][nx] != 0:
                    remain -= 1
                    w = w + buf[ny][nx][1]
                    max_w = max(w, max_w)
                    if buf[ny][nx][2] > idx:
                        idx = buf[ny][nx][2]
                        d = buf[ny][nx][0]
                buf[ny][nx] = [d, w, idx]
    mat = buf
    # print_mat(mat)
print(remain, max_w)