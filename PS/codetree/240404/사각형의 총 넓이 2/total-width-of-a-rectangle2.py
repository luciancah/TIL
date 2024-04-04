n = int(input())
positions = []
offset = 101
count = 0

matrix = [[0 for _ in range(202)] for _ in range(202)]
for i in range(n):
    positions += [list(map(int, input().split()))]
for x1, y1, x2, y2 in positions:
    x1, y1 = x1 + offset, y1 + offset
    x2, y2 = x2 + offset, y2 + offset
    for i in range(x1, x2):
        for j in range(y1, y2):
            matrix[i][j] += 1

for i in range(0, 202):
        for j in range(0, 202):
            if matrix[i][j] > 0:
                count += 1

print(count)