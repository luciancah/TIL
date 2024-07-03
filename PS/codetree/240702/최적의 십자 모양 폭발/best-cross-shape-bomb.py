import copy

n = int(input())
mat = []
for _ in range(n):
    mat.append([int(x) for x in input().split()])

def blow_up(row, col):
    r = mat[row][col]
    buf = copy.deepcopy(mat)
    for i in range(n):
        if abs(i - row) < r:
            buf[i][col] = 'x'
        if abs(i - col) < r:
            buf[row][i] = 'x'
    res = []
    for i in range(n):
        b = []
        for j in range(n-1, -1, -1):
            if buf[j][i] != 'x':
                b.append(buf[j][i])
        res.append(b)
    # print(row, col)
    # for l in res:
    #     print(*l)
    # print('---------------------')
    return res

def get_max_pair(rev_mat):
    region_max_pair = 0
    for i in range(n):
        for j in range(len(rev_mat[i])):
            if j < len(rev_mat[i]) - 1 and rev_mat[i][j] == rev_mat[i][j+1]:
                region_max_pair += 1
                # print(i, j, 'r')
            if i < n - 1 and len(rev_mat[i+1]) > j and rev_mat[i][j] == rev_mat[i+1][j]:
                region_max_pair += 1
                # print(i, j, 'b')
    # print(region_max_pair)
    return region_max_pair

max_pair = 0

for i in range(n):
    for k in range(n):
        max_pair = max(max_pair, get_max_pair(blow_up(i, k)))

print(max_pair)