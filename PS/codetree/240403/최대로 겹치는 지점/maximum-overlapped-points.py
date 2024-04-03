n = int(input())
positions = []
line = [0] * 101

for i in range(n):
    positions += [list(map(int, input().split()))]

for position in positions:
    start, end = position

    for x in range(start, end+1):
        line[x] += 1

print(max(line))