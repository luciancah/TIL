n, m, k = map(int, input().split())
arr = [input() for _ in range(n)]
sq = [list(map(int, input().split())) for _ in range(k)]

ps = [[[0, 0, 0] for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        for k in range(3):
            ps[i][j][k] = ps[i-1][j][k] + ps[i][j-1][k] - ps[i-1][j-1][k]
        if arr[i-1][j-1] == 'a':
            ps[i][j] = [ps[i][j][0] + 1, ps[i][j][1], ps[i][j][2]]
        elif arr[i-1][j-1] == 'b':
            ps[i][j] = [ps[i][j][0], ps[i][j][1] + 1, ps[i][j][2]]
        elif arr[i-1][j-1] == 'c':
            ps[i][j] = [ps[i][j][0], ps[i][j][1], ps[i][j][2] + 1]

# for i in range(n+1):
#     print(*ps[i])

for s in sq:
    r1, c1, r2, c2 = map(int, s)
    res = [0, 0, 0]
    for k in range(3):
        res[k] = ps[r2][c2][k] + ps[r1-1][c1-1][k] - ps[r2][c1-1][k] - ps[r1-1][c2][k]
    print(' '.join(map(str,res)))