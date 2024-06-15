from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
q = deque()
step = [[0 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y]:
        return False
    if grid[x][y] == 0:
        return False
    return True

def push(x, y, s):
    step[x][y] = s
    visited[x][y] = 1
    q.append((x, y))

def bfs():
    dxs, dys = [1, 0, 0, -1], [0, 1, -1, 0]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if can_go(nx, ny):
                push(nx, ny, step[x][y] + 1)

q = deque()
push(0, 0, 0)
bfs()

if step[-1][-1]:
    print(step[-1][-1])
else:
    print(-1)