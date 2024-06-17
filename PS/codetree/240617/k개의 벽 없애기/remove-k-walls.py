from collections import deque
from itertools import combinations

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
sr, sc = map(int, input().split())
er, ec = map(int, input().split())
sr, sc, er, ec = sr-1, sc-1, er-1, ec-1

walls = []
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            walls.append([i, j])

new_walls = list(combinations(walls, len(walls)-k))

# sr, sc = 0, 0
# er, ec = 0, 3

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_move(x, y):
    if not in_range(x, y):
        return False
    if new_grid[x][y]:
        return False
    if visited[x][y]:
        return False
    return True

def bfs():
    count = k
    dxs, dys = [1, 0, 0, -1], [0, 1, -1, 0]
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            dist = visited[x][y]
            nx, ny = x + dx, y + dy
            if can_move(nx, ny):
                if (nx, ny) == (er, ec):
                    return dist
                q.append((nx, ny))
                dist += 1
                visited[nx][ny] = dist

    return 9999

def create_grid(grid, walls):
    for w in walls:
        grid[w[0]][w[1]] = 1
    return grid

min_dist = 9999
for nw in new_walls:
    empty = [[0]*n for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    new_grid = create_grid(empty, nw)

    q = deque()

    q.append((sr, sc))
    visited[sr][sc] = 1
    dist = bfs()
    min_dist = min(dist, min_dist)

    # print(dist)
    # for i in range(n):
    #     print(*visited[i])
    # print()
    # for i in range(n):
    #     print(*new_grid[i])
    # print()
    

if min_dist == 9999:
    print(-1)
else:
    print(min_dist)