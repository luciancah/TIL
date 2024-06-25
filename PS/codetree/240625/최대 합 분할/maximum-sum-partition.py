import sys

INT_MIN = -sys.maxsize
OFFSET = 100000

n = int(input())
arr = [0] + list(map(int, input().split()))

m = sum(arr)
dp = [[0] * (m + 1 + OFFSET) for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(-m, m + 1):
        dp[i][j + OFFSET] = INT_MIN

dp[0][0 + OFFSET] = 0

def update(i, j, prev_i, prev_j, val):
    if prev_j < -m or prev_j > m or dp[prev_i][prev_j + OFFSET] == INT_MIN:
        return
    
    dp[i][j + OFFSET] = max(dp[i][j + OFFSET], dp[prev_i][prev_j + OFFSET] + val)

for i in range(1, n + 1):
    for j in range(-m, m + 1):
        update(i, j, i - 1, j - arr[i], arr[i])

        update(i, j, i - 1, j + arr[i], 0)

        update(i, j, i  - 1, j, 0)

print(dp[n][0 + OFFSET])