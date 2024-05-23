from copy import deepcopy

n = int(input())
grid = []

for _ in range(n):
    grid.append(list(map(int, input().split())))

def after_bomb(grid, r, c):
    new_grid = deepcopy(grid)
    spr = grid[r][c]-1
    for i in range(len(new_grid)):
        for j in range(len(new_grid)):
            if i == r:
                if abs(j - c) <= spr:
                    new_grid[i][j] = -1

            if j == c:
                if abs(i - r) <= spr:
                    new_grid[i][j] = -1

    return new_grid

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
    return list(map(list, zip(*new_grid)))


# grid = [[1, 0, 4, 3], [3, 2, 2, 3], [3, 2, 6, 2], [4, 5, 4, 4]]

def find_near(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid)-1):
            if grid[i][j] != 0 and grid[i][j] == grid[i][j+1]:
                count += 1
                j += 1

    grid2 = list(map(list, zip(*grid[::-1])))

    for i in range(len(grid2)):
        for j in range(len(grid2)-1):
            if grid2[i][j] != 0 and grid2[i][j] == grid2[i][j+1]:
                count += 1
                j += 1
            

    return count

# print(find_near(grid))

max_count = -9999
for i in range(len(grid)):
    for j in range(len(grid)):
        new_grid = push_grid(after_bomb(grid, i, j))
        count = find_near(new_grid)

        max_count = max(count, max_count)


print(max_count)

    # after_bomb(grid, by, bx)
    # grid = push_grid(grid)

    
# for i in range(len(grid)):
#     print(*grid[i])