from itertools import combinations
n, m = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
positive_dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if graph[i-1][j-1] > 0:
            positive_dp[i][j] = positive_dp[i-1][j] + positive_dp[i][j-1] - positive_dp[i-1][j-1] + 1
        else:
            positive_dp[i][j] = positive_dp[i-1][j] + positive_dp[i][j-1] - positive_dp[i-1][j-1]


def is_positive_rectangle(sx,sy,ex,ey,size):
    positive = positive_dp[ex][ey]-positive_dp[ex][sy-1]-positive_dp[sx-1][ey] + positive_dp[sx-1][sy-1]
    if size == positive:
        return True
    return False

ans = -1
for ax in range(1,n):
    for ay in range(1,m):
        for bx in range(ax,n+1):
            for by in range(ay,m+1):
                row = abs(ax-bx) + 1
                col = abs(ay-by) + 1
                size = row * col
                if is_positive_rectangle(ax,ay,bx,by,size):
                    ans = max(ans, size)
print(ans)


# 8만
# 양 누적합 (400)
# 총 누적합 (400)