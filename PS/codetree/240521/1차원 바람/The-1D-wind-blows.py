n, m, q = list(map(int, input().split()))
grid = []
wind = []

for _ in range(n):
    grid.append(list(map(str, input().split())))

for _ in range(q):
    wind.append(list(map(str, input().split())))
    

# 나랑 같은 index에 같은 숫자 있는지 확인하는 함수
def check_same_number(arr1, arr2):
    ans = False
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            ans = True        
    return ans

# 한바퀴 돌리는 함수
def push_array(arr, direc):
    new_arr = []
    if direc == 'R':
        temp = arr[0]
        for i in range(1, len(arr)):
            new_arr.append(arr[i])
        new_arr.append(temp)

    else:
        temp = arr[len(arr)-1]
        new_arr.append(temp)
        for i in range(len(arr)-1):
            new_arr.append(arr[i])
            
    return new_arr


if len(grid) == 1 and len(grid[0]) == 1:
    print(grid[0][0])

elif len(grid) == 1:
    for w in wind:
        grid_index = int(w[0]) - 1
        grid_dir = w[1]
        grid[grid_index] = push_array(grid[grid_index], w[1])
    for g in grid:
        print(*g)

else:
    for w in wind:
        spread = True
        grid_index = int(w[0]) - 1
        grid_dir = w[1]
        grid[grid_index] = push_array(grid[grid_index], w[1])

        # 위쪽 전파
        for i in range(grid_index, 0, -1):
            new_dir = 'L' if grid_dir == 'R' else 'R'
            if check_same_number(grid[i], grid[i - 1]):
                grid[i - 1] = push_array(grid[i - 1], new_dir)
                grid_dir = new_dir
            else:
                break


        # 아래쪽 전파
        grid_dir = w[1]
        for i in range(grid_index, len(grid)-1):
            new_dir = 'L' if grid_dir == 'R' else 'R'
            if check_same_number(grid[i], grid[i + 1]):
                grid[i + 1] = push_array(grid[i + 1], new_dir)
                grid_dir = new_dir
            else:
                break

    for g in grid:
        print(*g)