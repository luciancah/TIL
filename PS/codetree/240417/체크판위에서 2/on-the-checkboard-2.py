r, c = list(map(int, input().split()))
maps = []
for i in range(r):
    maps.append(list(map(str,input().split())))

count = 0
for i in range(1, r):
    for j in range(1, c):
        for k in range(i + 1, r - 1):
            for l in range(j + 1, c - 1):
                if maps[0][0] != maps[i][j] and \
                   maps[i][j] != maps[k][l] and \
                   maps[k][l] != maps[r-1][c-1]:
                    count += 1

print(count)