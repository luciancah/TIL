import sys

n = int(input())
grid = [input() for _ in range(n)]
coins = {}
start, end = [], []

for i in range(n):
    for j in range(n):
        if grid[i][j].isnumeric():
            coins[int(grid[i][j])] = [i, j]
        if grid[i][j] == 'S':
            start = [i, j]
        if grid[i][j] == 'E':
            end = [i, j]

coins = sorted(coins.items())
new_coins = {}
new_coins[0] = start

i = 1
for key, value in coins:
    new_coins[i] = value
    i += 1

new_coins[99] = end

if len(new_coins) < 5:
    print(-1)
    sys.exit()

def calc_dist(a, b):
    res = abs(a[0] - b[0]) + abs(a[1] - b[1])
    return res

min_dist = 9999

def recur(curr_coin, coin_count, move_dist):
    global min_dist
    if coin_count == 3:
        move_dist += calc_dist(new_coins[curr_coin], new_coins[99])
        min_dist = min(move_dist, min_dist)
        return

    for i in range(curr_coin+1, len(new_coins)-1):
        recur(i, coin_count+1, move_dist+calc_dist(new_coins[curr_coin], new_coins[i]))

recur(0, 0, 0)

print(min_dist)