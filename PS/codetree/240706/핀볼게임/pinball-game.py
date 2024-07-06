n = int(input())
mat = []
for _ in range(n):
    mat.append([int(x) for x in input().split()])

E = 0
S = 1
W = 2
N = 3

# E S W N
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

def turn(d, shape):
    if shape == 1:
        if d == E: return N
        elif d == W: return S
        elif d == N: return E
        elif d == S: return W
    elif shape == 2:
        if d == E: return S
        elif d == W: return N
        elif d == N: return W
        elif d == S: return E

def run_pinball(row, col, direction):
    time = 1
    x, y = col, row
    d = direction
    while x >= 0 and x <= n-1 and y >= 0 and y <= n-1:
        if mat[y][x] != 0:
            d = turn(d, mat[y][x])
        y, x = dys[d] + y, dxs[d] + x
        time += 1
    return time

max_time = 0
for i in range(4*n):
    if 0 <= i and i < n:
        row, col, direction = 0, i, S
    elif n <= i and i < 2*n:
        row, col, direction = i % n, n-1, W
    elif 2*n <= i and i < 3*n:
        row, col, direction = n-1, i % n, N
    else:
        row, col, direction = i % n, 0, E
    # print(row, col, direction)
    max_time = max(max_time, run_pinball(row, col, direction))
print(max_time)