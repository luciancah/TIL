# 선언시에 (n+1)*(m+1), -1로 초기화 해서 평균 구할때 빼고 구하기

n, m, q = list(map(int, input().split()))
grid = [[-1] * (m+2) for _ in range(n+2)]
wind = []

for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(len(arr)):
        grid[i+1][j+1] = arr[j]

for i in range(q):
    wind.append(list(map(int, input().split())))

# 한바퀴 돌리는 함수 (2차원 배열 받아서 2차원 배열 반환)
def turn_grid(grid):
    height = len(grid)
    width = len(grid[0])
    arr = []



    for i in range(width):
        arr.append(grid[0][i])

    for i in range(1, height-1):
        arr.append(grid[i][-1])

    for i in range(width-1, -1, -1):
        arr.append(grid[-1][i])

    for i in range(height-2, 0, -1):
        arr.append(grid[i][0])

    arr.insert(0, arr.pop())

    for i in range(width):
        grid[0][i] = arr[i]

    for i in range(width):
        grid[-1][i] = arr[len(arr)-1 - i - (height-2)]

    if height > 2:
        for i in range(height-2):
            grid[i+1][-1] = arr[width + i]

        for i in range(height-2):
            grid[i+1][0] = arr[len(arr)-1 - i]

    return grid

    

def get_mean(a, at, ar, ab, al):
    arr = [a, at, ar, ab, al]
    ans = 0
    count = 0

    for one in arr:
        if one != -1:
            ans += one
            count += 1

    return ans // count

for w in wind:
    new_grid = []
    
    for i in range(w[0], w[2]+1):
        new_grid.append(grid[i][w[1]:w[3]+1])

    new_grid = turn_grid(new_grid)
    count_i = 0
    for i in range(w[0], w[2]+1):
        count_j = 0
        for j in range(w[1], w[3]+1):
            grid[i][j] = new_grid[count_i][count_j]
            count_j += 1
        count_i += 1

    mean_grid = [[-1] * (m+2) for _ in range(n+2)]
    for i in range(w[0], w[2]+1):
        for j in range(w[1], w[3]+1):
            mean_grid[i][j] = get_mean(grid[i][j], grid[i-1][j], grid[i][j-1], grid[i][j+1], grid[i+1][j])

    for i in range(w[0], w[2]+1):
        for j in range(w[1], w[3]+1):
            grid[i][j] = mean_grid[i][j]
            
for i in range(1, n+1):
    print(*grid[i][1:m+1])


[[1, 6, 1, 0, 5],
[2, 2, 1, 6, 5],
[5, 2, 8, 8, 6]]

# [2, 1, 6, 1, 0, 5, 5, 6, 8, 8, 2, 5]

[[2, 1, 6, 1, 0],
[5, 2, 1, 6, 5],
[5, 6, 8, 8, 2]]