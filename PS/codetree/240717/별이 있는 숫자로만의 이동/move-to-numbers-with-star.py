n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ps = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        ps[i][j] = ps[i][j-1] + arr[i-1][j-1]

ans = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        sum_all = 0;
        for r in range(i - k, i + k + 1):
            c = k - abs(i - r);
            if 1 <= r and r <= n:
                sum_all += ps[r][min(j + c, n)] - ps[r][max(j - c - 1, 0)]
        
        ans = max(ans, sum_all)

print(ans)