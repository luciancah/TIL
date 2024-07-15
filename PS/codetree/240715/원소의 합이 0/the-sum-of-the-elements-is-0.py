from collections import defaultdict

n = int(input())
arrs = [list(map(int, input().split())) for _ in range(4)]

d1 = defaultdict(int)
d2 = defaultdict(int)

for i in range(n):
    for j in range(n):
        sum1 = arrs[0][i] + arrs[1][j]
        d1[sum1] += 1

        sum2 = arrs[2][i] + arrs[3][j]
        d2[sum2] += 1
        
ans = 0
for sum1 in d1:
    if -sum1 in d2:
        ans += d1[sum1] * d2[-sum1]

print(ans)