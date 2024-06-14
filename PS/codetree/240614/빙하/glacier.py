from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y]:
        return False
    if grid[x][y]:
        ices[x][y] = 1
        return False
    return True


q = deque()
dxs, dys = [1, 0, 0, -1], [0, 1, -1, 0]

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = 1
                q.append((nx, ny))

def calc_ice(grid):
    res = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                res += 1

    return res

def remove_ice(grid, ices):
    for i in range(n):
        for j in range(m):
            if ices[i][j]:
                grid[i][j] = 0
    
    return grid

ice_count = calc_ice(grid)
counts = []

while ice_count:
    visited = [[0]*m for _ in range(n)]
    ices = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    q.append((0, 0))
    bfs()
    ice_count = calc_ice(ices)
    counts.append(ice_count)
    grid = remove_ice(grid, ices)

print(len(counts)-1, counts[-2])