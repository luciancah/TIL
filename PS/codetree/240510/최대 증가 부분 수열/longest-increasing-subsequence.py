n = int(input())
lst = [int(x) for x in input().split()]
dp = [0 for _ in range(n)]
dp[0] = lst[0]
res = 1

for i in range(1, n):
    flag = 0
    for j in range(i):
        if dp[j] == 0:
            continue
        if lst[i] < dp[j]:
            flag = 1
            break
    if flag == 0:
        dp[i] = lst[i]
        res += 1

print(res)