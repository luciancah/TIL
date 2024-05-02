cmd = input()

mapper = {
    'N': 0,
    'W': 1,
    'S': 2,
    'E': 3
}

dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]
d = 0
x, y = 0, 0
t = 0
for i in range(len(cmd)):
    t += 1
    if cmd[i] == 'F':
        x += dxs[d]
        y += dys[d]
        if x == 0 and y == 0:
            print(t)
            exit()
    elif cmd[i] == 'R':
        d += 1
        d %= 4
    elif cmd[i] == 'L':
        d -= 1
        if d < 0:
            d += 4
print(-1)