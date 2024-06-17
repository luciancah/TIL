from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y]:
        return False
    if not grid[x][y] == 1:
        return False
    return True

def bfs():
    dxs, dys = [1, 0, 0, -1], [0, 1, -1, 0]
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            depth = visited[x][y]
            if can_go(nx, ny):
                depth += 1
                visited[nx][ny] = depth
                q.append((nx, ny))


starts = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            starts.append([i, j])

q = deque()
visited = [[0] * n for _ in range(n)]
for s in starts:
    q.append(s)
    visited[s[0]][s[1]] = 1
bfs()

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = visited[i][j] - 1
        visited[i][j] = visited[i][j] - 1

for i in range(n):
    print(*visited[i])