from collections import deque

n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
answer = [[0] * n for _ in range(n)]

'''
0: 이동가능
1: 벽
2: 사람
3: 피할곳
---
2 였던곳에 사람 최소거리
2 였던곳에 못가면 -1
'''

ppls = {}
dests = {}
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            ppls[(i, j)] = 0
        if grid[i][j] == 3:
            dests[(i, j)] = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if grid[x][y] == 1 or visited[x][y]:
        return False
    return True

def bfs():
    dxs, dys = [1, 0, 0, -1], [0, 1, -1, 0]

    while q:
        x, y = q.popleft()
        depth = visited[x][y]
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                if (nx, ny) in dests.keys():
                    return depth
                visited[nx][ny] = depth + 1
                q.append((nx, ny))

    return -1

for key, value in ppls.items():
    x, y = key
    q = deque()
    visited = [[0] * n for _ in range(n)]

    q.append((x, y))
    visited[x][y] = 1
    min_dist = bfs()

    # min_dist = 99999
    # for nkey, nvalue in dests.items():
    #     nx, ny = nkey
    #     if visited[nx][ny]:
    #         min_dist = min(min_dist, visited[nx][ny]-1)
    answer[x][y] = min_dist

for i in range(n):
    print(*answer[i])