n, m = map(int, input().split())
weights = []
values = []
dp = [[-1 for _ in range(m+1)] for _ in range(n)]

for _ in range(n):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

# dp[n] = n번 보석까지 고를 수 있을때 각 무게당 최대 가격

for i in range(n):
    dp[i][0] = 0

for i in range(n):
    for j in range(0, i+1):
        for k in range(m, -1, -1):
            if k >= weights[j]:
                dp[i][k] = max(dp[i][k], dp[i][k-weights[j]] + values[j])

# for i in range(n):
#     print(*dp[i])

print(max(dp[n-1]))