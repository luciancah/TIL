import sys
input = sys.stdin.readline

values = []
weights = []
n, m = map(int, input().split())
for _ in range(n):
    w, v = map(int, input().split())
    values.append(v)
    weights.append(w)

# dp배열 : 무게 / 금액 / 개수 ?

dp = [-1 for _ in range(m+1)]
dp[0] = 0

for j in range(1, m+1):
    for k in range(n):
        if j >= weights[k]:
            if dp[j-weights[k]] == -1:
                continue
            dp[j] = max(dp[j], dp[j-weights[k]] + values[k])

print(max(dp))