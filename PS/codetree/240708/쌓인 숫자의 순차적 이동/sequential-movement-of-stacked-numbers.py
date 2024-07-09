n, m = map(int, input().split())
global mat
mat = []
for _ in range(n):
    mat.append([[int(x)] for x in input().split()])

def print_mat():
    for l in mat:
        print(*l)

def move_to_max_neighbor(row, col, target):
    region_max = 0
    targ_row, targ_col = row, col
    if row > 0 and col > 0 and len(mat[row-1][col-1]) and max(mat[row-1][col-1]) >= region_max: # upper left
        region_max = max(mat[row-1][col-1])
        targ_row, targ_col = row-1, col-1
    if row > 0 and len(mat[row-1][col]) and max(mat[row-1][col]) >= region_max: # upper middle
        region_max = max(mat[row-1][col])
        targ_row, targ_col = row-1, col
    if row > 0 and col < n - 1 and len(mat[row-1][col+1]) and max(mat[row-1][col+1]) >= region_max: # upper right
        region_max = max(mat[row-1][col+1])
        targ_row, targ_col = row-1, col+1
    if col < n - 1 and len(mat[row][col+1]) and max(mat[row][col+1]) >= region_max: # right middle
        region_max = max(mat[row][col+1])
        targ_row, targ_col = row, col+1
    if row < n - 1 and col < n - 1 and len(mat[row+1][col+1]) and max(mat[row+1][col+1]) >= region_max: # bottom right
        region_max = max(mat[row+1][col+1])
        targ_row, targ_col = row+1, col+1
    if row < n - 1 and len(mat[row+1][col]) and max(mat[row+1][col]) >= region_max: # bottom middle
        region_max = max(mat[row+1][col])
        targ_row, targ_col = row+1, col
    if row < n - 1 and col > 0 and len(mat[row+1][col-1]) and max(mat[row+1][col-1]) >= region_max: # bottom left
        region_max = max(mat[row+1][col-1])
        targ_row, targ_col = row+1, col-1
    if col > 0 and len(mat[row][col-1]) and max(mat[row][col-1]) >= region_max: # left middle
        region_max = max(mat[row][col-1])
        targ_row, targ_col = row, col-1
    if targ_row != row or targ_col != col:
        idx = mat[row][col].index(target)
        buf = mat[row][col][idx:]
        mat[row][col] = mat[row][col][:idx]
        for i in buf:
            mat[targ_row][targ_col].append(i)
    # print_mat()
    # print(target, row, col)


to_move = ([int(x) for x in input().split()])
for target in to_move:
    found = False
    for row in range(n):
        if found: break
        for col in range(n):
            if found: break
            if target in mat[row][col]:
                move_to_max_neighbor(row, col, target)
                found = True

for i in range(n):
    for j in range(n):
        if len(mat[i][j]) == 0:
            print("None")
        else:
            print(*reversed(mat[i][j]))