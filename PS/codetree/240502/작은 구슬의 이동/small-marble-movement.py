n, t = map(int, input().split())
r, c, d = input().split()
r = int(r) - 1
c = int(c) - 1

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

mapper = {
    'D': 0,
    'R': 1,
    'U': 2,
    'L': 3
}
# print(n, t)
# print(c, r)

for _ in range(t):
    move_dir = mapper[d]
    nx = c + dxs[move_dir]
    ny = r + dys[move_dir]
    if nx >= n:
        # print('LEFT')
        d = 'L'
    elif nx < 0:
        # print('RIGHT')
        d = 'R'
    elif ny >= n:
        # print('UP')
        d = 'U'
    elif ny < 0:
        # print('DOWN')
        d = 'D'
    else:
        c = nx
        r = ny
        # print(c, r)

print(r + 1, c + 1)