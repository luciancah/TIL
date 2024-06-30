n, m, q = map(int, input().split())
mat = []
for _ in range(n):
    mat.append([int(x) for x in input().split()])

def shift_clockwise(r1, c1, r2, c2):
    temp1 = mat[r1][c2]
    for i in range(c2, c1, -1):
        mat[r1][i] = mat[r1][i-1]
    temp2 = mat[r2][c2]
    for j in range(r2, r1, -1):
        if j == r1 + 1:
            mat[j][c2] = temp1
        else:
            mat[j][c2] = mat[j-1][c2]
    temp3 = mat[r2][c1]
    for k in range(c1, c2):
        if k == c2 - 1:
            mat[r2][k] = temp2
        else:
            mat[r2][k] = mat[r2][k+1]
    for l in range(r1, r2):
        if l == r2 - 1:
            mat[l][c1] = temp3
        else:
            mat[l][c1] = mat[l+1][c1]

def get_point_mean(i, j):
    res = mat[i][j]
    if i > 0:
        res += mat[i-1][j]
    if i < n-1:
        res += mat[i+1][j]
    if j > 0:
        res += mat[i][j-1]
    if j < m-1:
        res += mat[i][j+1]
    return res

def transform_mean(r1, c1, r2, c2):
    buf = []
    for i in range(r1, r2 + 1):
        row = []
        for j in range(c1, c2 + 1):
            div = 5
            if i == 0 or i == n - 1:
                div -= 1
            if j == 0 or j == m - 1:
                div -= 1
            row.append(get_point_mean(i, j) // div)
            # row.append(sum([
            #     mat[k][l]
            #     for k in range (n)
            #     for l in range (m)
            #     if abs(k-i) + abs(l-j) <= 1
            #     ]) // div)
        buf.append(row)
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            mat[i][j] = buf[i-r1][j-c1]

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1
    shift_clockwise(r1, c1, r2, c2)
    transform_mean(r1, c1, r2, c2)

for l in mat:
    print(*l)