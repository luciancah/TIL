n = int(input())
grid = []
directions = []

for _ in range(n):
    grid.append(list(map(int, input().split())))

for _ in range(n):
    directions.append(list(map(int, input().split())))

r, c = list(map(int, input().split()))
r, c = r-1, c-1

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

ans = []
    
dirs = {
    1: [-1, 0],
    2: [-1, 1],
    3: [0, 1],
    4: [1, 1],
    5: [1, 0],
    6: [1, -1],
    7: [0, -1],
    8: [-1, -1]
}

max_dist = 0

def recur(r,c,d,count):
    global max_dist
    # print(r, c, count , grid[r][c])
    max_dist = max(count, max_dist)
    # if not in_range(r, c):
    #     # print(count)
    #     return

    for i in range(1, n):
        nr, nc = r + i*dirs[d][0], c + i*dirs[d][1]
        if not in_range(nr, nc):
            max_dist = max(count, max_dist)
            # print(count)
            continue
        if grid[nr][nc] > grid[r][c]:
            recur(nr, nc, directions[nr][nc], count+1)

recur(r, c, directions[r][c], 0)

print(max_dist)