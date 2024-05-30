import sys
sys.setrecursionlimit(10000)

n = int(input())
grid = []
bombs = []
bombs_placed = []
bp2 = []
bp3 = []

bomb_spreads = [[[-1, 0], [-2, 0], [1, 0], [2, 0]], [[-1, 0], [1, 0], [0, 1], [0, -1]], [[-1, -1], [1, 1], [-1, 1], [1, -1]]]

for _ in range(n):
    grid.append(list(map(int, input().split())))

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def spread_bomb(r, c, t):
    new_bombs = []
    for i in range(4):
        ny, nx = r + bomb_spreads[t][i][0], c + bomb_spreads[t][i][1]
        if in_range(ny, nx):
            new_bombs.append([ny, nx])

    return new_bombs

for r in range(n):
    for c in range(n):
        if grid[r][c] == 1:
            bombs.append([r, c])

def place_bomb(bombs_count):
    if bombs_count == len(bombs) + 1:
        bp3.append(bp2[:])
        return

    for i in range(3):
        bombs_placed.append(i)
        bp2.append(spread_bomb(bombs[bombs_count-1][0], bombs[bombs_count-1][1], i))
        place_bomb(bombs_count + 1)
        bp2.pop()
        bombs_placed.pop()
    
place_bomb(1)

bp4 = []
for i in range(len(bp3)):
    new = []
    for j in range(len(bp3[i])):
        new += bp3[i][j]
    new += bombs
    bp4 += [new]

bp5 = []
for i in range(len(bp4)):
    bp5.append(len(set([tuple(set(bp4[i])) for bp4[i] in bp4[i]])))

print(max(bp5))