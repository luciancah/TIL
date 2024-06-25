n, m = map(int, input().split())
mat = []
for _ in range(n):
    mat.append(input().split())
res = 0

for i in range(n):
    prev = mat[i][0]
    streak = 1
    if streak >= m:
        res += 1
        continue
    for k in range(1, n):
        if prev == mat[i][k]:
            streak += 1
        else:
            streak = 1
        if streak >= m:
            res += 1
            break
        prev = mat[i][k]

for i in range(n):
    prev = mat[0][i]
    streak = 1
    if streak >= m:
        res += 1
        continue
    for k in range(1, n):
        if prev == mat[k][i]:
            streak += 1
        else:
            streak = 1
        if streak >= m:
            res += 1
            break
        prev = mat[k][i]

print(res)