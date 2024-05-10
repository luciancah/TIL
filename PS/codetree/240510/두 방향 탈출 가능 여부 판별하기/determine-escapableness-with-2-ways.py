n, m = map(int, input().split())
snake = [[int(x) for x in input().split()] for i in range(n)]
visited = [[False for col in range(m)] for row in range(n)]
dxs, dys = [0, 1], [1, 0] # 오른쪽, 아래

res = 0

def dfs(x, y):
    if x == m - 1 and y == n - 1:
        print(1)
        exit()
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if m > nx >= 0 and n > ny >= 0 and snake[ny][nx] == 1 and visited[ny][nx] == False:
            visited[ny][nx] = True
            dfs(nx, ny)
dfs(0, 0)
print(res)