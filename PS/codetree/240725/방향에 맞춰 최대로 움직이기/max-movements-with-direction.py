n = int(input())
mat = []
dir_mat = []
for _ in range(n):
    mat.append([int(x) for x in input().split()])
for _ in range(n):
    dir_mat.append([int(x) for x in input().split()])
row, col = map(int, input().split())
max_move = 0

# ↑, ↗, →, ↘, ↓, ↙, ←, ↖
dxs, dys = [0, 1, 1, 1, 0, -1, -1, -1], [-1, -1, 0, 1, 1, 1, 0, -1]

def is_end(curr_val, d, row, col):
    ny, nx = row + dys[d], col + dxs[d]
    initial_val = curr_val

    if ny < 0 or ny > n - 1 or nx < 0 or nx > n - 1:
        return True
    
    while not (ny < 0 or ny > n - 1 or nx < 0 or nx > n - 1):
        curr_val = max(curr_val, mat[ny][nx])
        ny, nx = ny + dys[d], nx + dxs[d]
    
    if initial_val == curr_val: return True
    return False

def run(row, col, curr_move):
    global max_move
    # print(row, col, curr_move)
    d = dir_mat[row][col] - 1
    val = mat[row][col]

    if is_end(val, d, row, col):
        max_move = max(max_move, curr_move)
        # print('END: ', row, col, max_move)
        return

    init_val = mat[row][col]
    row, col = row + dys[d], col + dxs[d]
    while not (row < 0 or row > n - 1 or col < 0 or col > n - 1):
        if mat[row][col] > init_val:
            run(row, col, curr_move + 1)
        row, col = row + dys[d], col + dxs[d]
    
run(row - 1, col - 1, 0)
print(max_move)