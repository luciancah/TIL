n = 3
positions = []
offset = 1001
count = 0

matrix = [[0 for _ in range(2002)] for _ in range(2002)]
for i in range(n):
    positions += [list(map(int, input().split()))]
for index, values in enumerate(positions):
    x1, y1, x2, y2 = values
    c = 1 if index != 2 else -1
    x1, y1 = x1 + offset, y1 + offset
    x2, y2 = x2 + offset, y2 + offset
    for i in range(x1, x2):
        for j in range(y1, y2):
            matrix[i][j] += c

for i in range(0, 2002):
        for j in range(0, 2002):
            if matrix[i][j] == 1:
                count += 1

print(count)