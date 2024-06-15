from collections import deque

n = int(input())
sr, sc, er, ec = map(int, input().split())

# 나이트 이동 경로 = 2r, 1c or 1r, 2c
dxs, dys = [-2, -1, 1, 2, 2, 1, -1, -2], [-1, -2, -2, -1, 1, 2, 2, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y]:
        return False
    return True

q = deque()

def bfs():
    while q:
        x, y = q.popleft()
        depth = visited[x][y]
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = depth + 1
                q.append((nx, ny))

visited = [[0] * n for _ in range(n)]

visited[sr-1][sc-1] = 1
q.append((sr-1, sc-1))
bfs()

# for i in range(n):
#     print(*visited[i])

if visited[er-1][ec-1]:
    print(visited[er-1][ec-1]-1)
else:
    print(-1)