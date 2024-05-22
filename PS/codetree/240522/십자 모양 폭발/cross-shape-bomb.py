n = int(input())
grid = []
bomb = []

for _ in range(n):
    grid.append(list(map(int, input().split())))

bomb = list(map(int, input().split()))

def after_bomb(grid, r, c):
    spr = grid[r][c]-1
    for i in range(len(grid)):
        for j in range(len(grid)):
            if i == r:
                if abs(j - c) <= spr:
                    grid[i][j] = -1

            if j == c:
                if abs(i - r) <= spr:
                    grid[i][j] = -1

def push_grid(grid):
    new_grid = []
    for i in range(len(grid)):
        temp_arr = []
        count = 0
        for j in range(len(grid)):
            if grid[j][i] != -1:
                temp_arr.append(grid[j][i])
                count += 1

        for _ in range(count, len(grid)):
            temp_arr.insert(0, 0)

        new_grid.append(temp_arr)

    for i in range(len(grid)):
        for j in range(len(grid)):
            print(new_grid[j][i], end = ' ')
        print()


after_bomb(grid, bomb[0]-1, bomb[1]-1)
push_grid(grid)