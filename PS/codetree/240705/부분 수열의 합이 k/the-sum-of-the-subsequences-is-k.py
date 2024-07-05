n, k = map(int, input().split())
arr = list(map(int, input().split()))

ps = [0 for _ in range(n+1)]
for i in range(1, n+1):
    ps[i] = ps[i-1] + arr[i-1]

ans = 0
for i in range(n+1):
    for j in range(i, n+1):
        if ps[j] - ps[i] == k:
            ans += 1
        if ps[j] - ps[i] > k:
            break

print(ans)