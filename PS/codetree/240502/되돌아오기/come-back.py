n = int(input())

mapper = {
    'N' : 0,
    'S' : 1,
    'W' : 2,
    'E' : 3
}
dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]
x, y = 0, 0
t = 0
for _ in range(n):
    d, offset = input().split()
    offset = int(offset)
    for i in range(offset):
        nx, ny = x + dxs[mapper[d]], y + dys[mapper[d]]
        t += 1
        if nx == 0 and ny == 0:
            print(t)
            exit()
        x, y = nx, ny
print(-1)