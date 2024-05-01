n, t = map(int, input().split())
r, c, d = input().split()
r = int(r) - 1
c = int(c) - 1

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

mapper = {
    'U': 0,
    'R': 1,
    'D': 2,
    'L': 3
}

for i in range(t):
    move_dir = mapper[d]
    nx = c + dxs[move_dir]
    ny = r + dys[move_dir]
    if nx >= n-1:
        d = 'L'
    elif nx < 0:
        d = 'R'
    elif ny >= n-1:
        d = 'D'
    elif ny < 0:
        d = 'U'
    else:
        c = nx
        r = ny

print(r + 1, c + 1)