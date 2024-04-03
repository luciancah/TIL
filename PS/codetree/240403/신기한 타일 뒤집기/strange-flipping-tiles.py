n = int(input())
positions = []
current = 5000


line = [''] * 10001
for i in range(n):
    positions += [list(map(str, input().split()))]

for position in positions:
    dist, direction = position

    if direction == 'L':
        for i in range(int(dist)):
            line[current - i] = 'white'
        current -= int(dist) - 1

    if direction == 'R':
        for i in range(int(dist)):
            line[current + i] = 'black'
        current += int(dist) - 1


print(len([x for x in line if x == 'white']), len([x for x in line if x == 'black']))