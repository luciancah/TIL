n, m = map(int, input().split())
mat = []
for _ in range(n):
    mat.append([int(x) for x in input().split()])

# 2x2 sector for block 1
val = 0
for i in range(n - 1):
    for j in range(m - 1):
        frame_val = mat[i][j] + mat[i+1][j] + mat[i+1][j+1] + mat[i][j+1]
        candidate = frame_val - min(mat[i][j], mat[i+1][j], mat[i+1][j+1], mat[i][j+1])
        val = max(val, candidate)

# 3x3 sector for block 2
for i in range(n - 2):
    for j in range(m - 2):
        for k in range(3):
            val = max(mat[i+k][j] + mat[i+k][j+1] + mat[i+k][j+2],
             mat[i][j+k] + mat[i+1][j+k] + mat[i+2][j+k], val)

print(val)