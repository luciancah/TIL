n, q = map(int, input().split())
rocks = [[0 for _ in range(n)] for _ in range(3)]

for i in range(n):
    rocks[int(input())-1][i] = 1

rg = [list(map(int, input().split())) for _ in range(q)]
ps = [[0 for _ in range(n+1)] for _ in range(3)]

for i in range(3):
    for j in range(1, n+1):
        ps[i][j] = ps[i][j-1] + rocks[i][j-1]

for r in rg:
    ans = []
    for i in range(3):
        ans.append(ps[i][r[1]] - ps[i][r[0]-1])
    print(' '.join(map(str, ans)))