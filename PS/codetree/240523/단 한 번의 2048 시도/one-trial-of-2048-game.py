grid = []
for _ in range(4):
    grid.append(list(map(int, input().split())))

direction = input()

def rotate_cw(arr):
    return list(map(list, zip(*arr[::-1])))

def rotate_ccw(arr):
    return list(map(list, zip(*arr)))[::-1]

# [0 0 0 4]

# [0 2 0 2]
# 왼쪽에서 오른쪽으로 순회하면서 - 같은거 있는지 본 다음 - 같은거 있으면 묶고 - 새 배열에 어펜드 - 4 길이 맞춰서 0 채우기

def push_list(arr):
    new_arr1 = []
    new_arr2 = []

    # 1. 0 제거
    for i in range(4):
        if arr[i] != 0:
            new_arr1.append(arr[i])

    # 2. 왼쪽으로 땡기기
    i = 0
    new_arr1 += [0]
    while i < len(new_arr1)-1:
        if new_arr1[i] == new_arr1[i+1]:
            new_arr2.append(new_arr1[i] * 2)
            i += 2
        else:
            new_arr2.append(new_arr1[i])
            i += 1

    # 3. 길이 4로 맞추기 <- 이건 방향때뭉네 다시 봐야할듯
    for _ in range(4-len(new_arr2)):
        new_arr2.append(0)

    return new_arr2

# 풀이

answer_grid = []

if direction == 'L':
    for i in range(4):
        answer_grid.append(push_list(grid[i]))

if direction == 'R':
    grid = rotate_cw(grid)
    grid = rotate_cw(grid)
    
    for i in range(4):
        answer_grid.append(push_list(grid[i]))

    answer_grid = rotate_cw(answer_grid)
    answer_grid = rotate_cw(answer_grid)

if direction == 'U':
    grid = rotate_ccw(grid)

    for i in range(4):
        answer_grid.append(push_list(grid[i]))

    answer_grid = rotate_cw(answer_grid)

if direction == 'D':
    grid = rotate_cw(grid)

    for i in range(4):
        answer_grid.append(push_list(grid[i]))

    answer_grid = rotate_ccw(answer_grid)



for i in range(4):
    print(*answer_grid[i])