n = int(input())
positions = []
offset = 101
count = 0

matrix = [[0 for _ in range(202)] for _ in range(202)]
for i in range(n):
    positions += [list(map(int, input().split()))]
for index, values in enumerate(positions):
    x1, y1 = values
    x1, y1 = x1 + offset, y1 + offset
    x2, y2 = x1 + 8, y1 + 8
    for i in range(x1, x2):
        for j in range(y1, y2):
            matrix[i][j] += 1

for i in range(0, 202):
        for j in range(0, 202):
            if matrix[i][j]:
                count += 1

print(count)