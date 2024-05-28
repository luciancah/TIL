n = int(input())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

dys, dxs = [-1, 1, 0, 0], [0, 0, 1, -1]
move_dirs = {'U': 0, 'D': 1, 'R': 2, 'L': 3}

ball_path = []

def change_dir(curr_dir, pin):
    direction_map = {
        'R': {1: 'U', 2: 'D'},
        'L': {1: 'D', 2: 'U'},
        'U': {1: 'R', 2: 'L'},
        'D': {1: 'L', 2: 'R'}
    }
    return direction_map[curr_dir][pin]

def simulate_ball(y, x, curr_dir):
    # print('start', y, x, curr_dir)
    count = 1
    if grid[y][x] == 1:
        curr_dir = change_dir(curr_dir, 1)
    if grid[y][x] == 2:
        curr_dir = change_dir(curr_dir, 2)
    while (count <= n*n*n):
        # print(curr_dir, y, x)
        ny, nx = y + dys[move_dirs[curr_dir]], x + dxs[move_dirs[curr_dir]]
        count += 1
        if not in_range(ny, nx):
            # print('out', count)
            return count
        # 1일때
        if grid[ny][nx] == 1:
            curr_dir = change_dir(curr_dir, 1)
        
        if grid[ny][nx] == 2:
            curr_dir = change_dir(curr_dir, 2)
        

        y, x = ny, nx

    return -1

max_count = 0

# 시뮬레이션
for i in range(n):
    y, x = 0, i
    curr_dir = 'D'
    count = simulate_ball(y, x, curr_dir)
    max_count = max(max_count, count)

    y, x = n-1, i
    curr_dir = 'U'
    count = simulate_ball(y, x, curr_dir)
    max_count = max(max_count, count)

    y, x = i, 0
    curr_dir = 'R'
    count = simulate_ball(y, x, curr_dir)
    max_count = max(max_count, count)

    y, x = i, n-1
    curr_dir = 'L'
    count = simulate_ball(y, x, curr_dir)
    max_count = max(max_count, count)

print(max_count)

# 2 1 0 2 
# 2 0 2 2 
# 1 2 1 2 
# 2 0 2 1

# \ / 0 \
# \ 0 \ \
# / \ / \
# \ 0 \ /

# 0 2 
# 0 1

# 0 \
# 0 /