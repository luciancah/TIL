n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_move(x, y, curr_num):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] != curr_num:
        return False
    return True

dxs, dys = [1, 0, 0, -1], [0, 1, -1, 0]

blocks = []
def dfs(x, y):
    global size
    for i in range(4):
        nx, ny = x + dxs[i], y + dys[i]
        if can_move(nx, ny, grid[x][y]):
            visited[nx][ny] = True
            size += 1
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        size = 0
        if not visited[i][j]:
            visited[i][j] = True
            size += 1
            dfs(i, j)
        if size != 0:
            blocks.append(size)

print(len([x for x in blocks if x >= 4]), max(blocks))