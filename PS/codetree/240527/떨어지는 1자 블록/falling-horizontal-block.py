n, m, k = list(map(int, input().split()))
grid = []

for _ in range(n):
    grid.append(list(map(int, input().split())))

end_col = 0

flag = True
i = 0
while (flag and i < n):
    for j in range(k-1, k-1+m):
        if grid[i][j] == 1:
            end_col = i-1
            flag = False
    i += 1

if flag:
    end_col = n-1

for j in range(k-1, k-1+m):
    grid[end_col][j] = 1

for i in range(n):
    print(*grid[i])