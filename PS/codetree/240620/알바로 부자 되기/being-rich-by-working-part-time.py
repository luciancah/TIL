n = int(input())
grid = []
dp = [0] * n
for _ in range(n):
    grid.append(list(map(int, input().split())))

# 알바 정보: s, e, p = 시작, 끝, 돈 // 시작 순서대로 정렬되어 있음
# dp 배열 : 해당 일자에 일 했을때 벌 수 있는 최대 돈

dp[0] = grid[0][2]
for i in range(1, n):
    max_money = 0
    for j in range(0, i):
        if grid[j][1] < grid[i][0]:
            max_money = max(grid[i][2] + dp[j], max_money)
        else:
            max_money = max(max_money, grid[i][2])
    dp[i] = max_money
# print(dp)
print(max(dp))