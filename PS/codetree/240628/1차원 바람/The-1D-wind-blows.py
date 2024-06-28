n, m, q = map(int, input().split())
mat = []
for _ in range(n):
    mat.append([int(x) for x in input().split()])

def shift(target_row, direction):
    if direction == 'R':
        temp = mat[target_row][0]
        for i in range(m-1):
            mat[target_row][i] = mat[target_row][i+1]
        mat[target_row][m-1] = temp
    if direction == 'L':
        temp = mat[target_row][m-1]
        for i in range(m-1, 0, -1):
            mat[target_row][i] = mat[target_row][i-1]
        mat[target_row][0] = temp

def propagate_up(target_row, prev_dir):
    if target_row < 0:
        return
    for i in range(m):
        if mat[target_row+1][i] == mat[target_row][i]:
            if prev_dir == 'L':
                shift(target_row, 'R')
                propagate_up(target_row-1, 'R')
            else:
                shift(target_row, 'L')
                propagate_up(target_row-1, 'L')
            break

def propagate_down(target_row, prev_dir):
    if target_row > n-1:
        return
    for i in range(m):
        if mat[target_row-1][i] == mat[target_row][i]:
            if prev_dir == 'L':
                shift(target_row, 'R')
                propagate_down(target_row+1, 'R')
            else:
                shift(target_row, 'L')
                propagate_down(target_row+1, 'L')
            break

for _ in range(q):
    wind_row, direction = input().split()
    wind_row = int(wind_row) - 1
    shift(wind_row, direction)
    propagate_down(wind_row+1, direction)
    propagate_up(wind_row-1, direction)

for l in mat:
    print(*l)