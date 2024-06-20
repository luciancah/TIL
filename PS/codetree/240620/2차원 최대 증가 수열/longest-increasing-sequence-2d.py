n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]

dp[0][0] = 1

# for i in range(n):
#     print(*dp[i])
# print()

for i in range(1, n):
    for j in range(1, m):
        new_count = 0
        for k in range(0, i+1):
            for l in range(0, j+1):
                if k == i or l == j:
                    continue
                if grid[i][j] > grid[k][l] and dp[k][l] != 0:
                    # print(i, j, k, l, grid[i][j], grid[k][l])
                    new_count = max(new_count, dp[k][l]+1)
        dp[i][j] = new_count

# for i in range(n):
#     print(*dp[i])

ans = 0            
for i in range(n):
    ans = max(ans, max(dp[i]))

print(ans)