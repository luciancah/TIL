import sys

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
ps = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        ps[i][j] = ps[i][j-1] + ps[i-1][j] - ps[i-1][j-1] + grid[i-1][j-1]

ans = -sys.maxsize

def get_sum(x1, y1, x2, y2):
    return ps[x2][y2] - ps[x1-1][y2] - ps[x2][y1-1] + ps[x1-1][y1-1]

for i in range(1, n+1):
    for j in range(i, n+1):
        dp = [0] * (n+1)

        for y in range(1, n+1):
            value = get_sum(i, y, j, y)
            dp[y] = max(value, dp[y-1] + value)
        
        max_area = -sys.maxsize
        for y in range(1, n+1):
            max_area = max(max_area, dp[y])

        ans = max(ans, max_area)

print(ans)