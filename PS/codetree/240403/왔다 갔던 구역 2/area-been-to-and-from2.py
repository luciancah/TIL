n = int(input())
positions = []
current = 500
line = [0] * 1001
for i in range(n):
    positions += [list(map(str, input().split()))]

for position in positions:
    dist, direction = position

    if direction == 'L':
        for _ in range(int(dist)):
            current -= 1
            line[current] += 1

    if direction == 'R':
        for _ in range(int(dist)):
            current += 1
            line[current - 1] += 1



print(len([x for x in line if x >= 2]))