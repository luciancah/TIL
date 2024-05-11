import sys

INT_MIN = -sys.maxsize

n = int(input())
mat = [[int(x) for x in input().split()] for i in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

def print_mat(m):
    for elem in m:
        print(elem)

def init():
    s = 0
    for i in range(n):
        s += mat[i][0]
        dp[i][0] = s
    s = 0
    for i in range(n):
        s += mat[i][i]
        dp[i][i] = s
    s = 0
    for i in range(n):
        s += mat[0][i]
        dp[0][i] = s

def fill():
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i-1][j] + mat[i][j], dp[i][j-1] + mat[i][j])

res = INT_MIN


init()
fill()
for i in range(n):
    res = max(res, dp[-1][i])
# print_mat(dp)
print(res)