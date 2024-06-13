from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
starts = [list(map(int, input().split())) for _ in range(m)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 1:
        return False
    return True

def push(x, y):
    answer[x][y] = 1
    visited[x][y] = True
    q.append((x, y))


def bfs():
    dxs, dys = [1, 0, 0, -1], [0, 1, -1, 0]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                push(nx, ny)

answer = [[0 for _ in range(n)] for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

q = deque()
for start in starts:
    push(start[0]-1, start[1]-1)
bfs()

res = 0
for i in range(n):
    for j in range(n):
        if answer[i][j]:
            res += 1

print(res)