n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y <n

def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    
    max_length = 1
    # dxs, dys = [1, 0, 0, -1], [0, 1, -1, 1]
    dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[nx][ny] > grid[x][y]:
            length = 1 + dfs(nx, ny)
            max_length = max(max_length, length)
    
    dp[x][y] = max_length
    return max_length

max_path = 0
for i in range(n):
    for j in range(n):
        max_path = max(max_path, dfs(i, j))

print(max_path)