from collections import deque
from itertools import combinations

n, k, d, u = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, num):
    if not in_range(x, y):
        return False
    if visited[x][y]:
        return False
    if not (d <= abs(grid[x][y] - num) <= u):
        # print('걸림', d, abs(grid[x][y] - num), u)
        return False
    return True

dxs, dys = [1, 0, 0, -1], [0, 1, -1, 0]

def bfs():
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            num = grid[x][y]
            if can_go(nx, ny, num):
                q.append((nx, ny))
                visited[nx][ny] = 1

nodes = []

for i in range(n):
    for j in range(n):
        nodes.append([i, j])

selected_nodes = list(combinations(nodes, k))

def count_visited(grid):
    res = 0

    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                res += 1

    return res

max_visited = 0

for sn in selected_nodes:
    visited = [[0]*n for _ in range(n)]
    q = deque()
    for s in sn:
        q.append((s[0], s[1]))
        visited[s[0]][s[1]] = 1
        bfs()

        # print('iteration', s)
        # for i in range(n):
        #     print(*visited[i])
        # print()

    cv = count_visited(visited)
    max_visited = max(cv, max_visited)

print(max_visited)