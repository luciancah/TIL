n = int(input())
m = []
for _ in range(n):
    m.append(input().split())

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

total = 0
for y in range(n):
    for x in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if ny >= 0 and nx >= 0 and ny < n and nx < n and m[ny][nx] == '1':
                cnt += 1
        if cnt >= 3:
            total += 1

print(total)