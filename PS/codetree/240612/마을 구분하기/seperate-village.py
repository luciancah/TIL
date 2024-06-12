n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
answer = [[0 for _ in range(n)] for _ in range(n)]
order = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

def dfs(x, y):
    global order

    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if can_go(nx, ny):
            answer[nx][ny] = order
            order += 1
            visited[nx][ny] = 1
            dfs(nx, ny)

vils = []

for i in range(n):
    for j in range(n):
            prev_order = order
            if can_go(i, j):
                order = 1
                visited[i][j] = 1
                answer[i][j] = order
                dfs(i, j)
                vils.append(order)

print(len(vils))
vils.sort()
for i in range(len(vils)):
    print(vils[i])